"""Import activities from the external Bored API into local storage."""

import logging
import time
import requests

from decimal import Decimal, InvalidOperation
from functools import cache

from activities.models import Activity
from activities.const import BORED_API_URL, DEFAULT_IMPORT_COUNT, DEFAULT_IMPORT_TIMEOUT


logger = logging.getLogger(__name__)

def import_activities(
    count=DEFAULT_IMPORT_COUNT,
    timeout=DEFAULT_IMPORT_TIMEOUT,
    time_provider=None,
):
    """Fetch and upsert activities until count is reached or timeout expires."""
    
    tp = time_provider or time.time
    start = tp()
    added = skipped = 0
    errors = []

    for _ in range(count):
        try:
            response = requests.get(BORED_API_URL)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            logger.exception("Failed to fetch activity from API")
            errors.append("network error")
            skipped += 1
            if tp() - start > timeout:
                break
            continue
        except ValueError:
            logger.exception("Failed to decode activity payload from API")
            skipped += 1
            if tp() - start > timeout:
                break
            continue
 

        key = data.get("key")
        if key is None:
            logger.warning("Skipping activity because API payload is missing 'key': %s", data)
            skipped += 1
            if tp() - start > timeout:
                break
            continue

        raw_participants = data.get("participants", 0)
        raw_price = data.get("price", 0)
        try:
            participants = int(raw_participants)
            price = Decimal(str(raw_price))
        except (TypeError, ValueError, InvalidOperation):
            logger.warning(
                "Skipping activity with invalid numeric fields: key=%s participants=%r price=%r",
                key,
                raw_participants,
                raw_price,
            )
            skipped += 1
            if tp() - start > timeout:
                break
            continue

        defaults = {
            "activity": data.get("activity", ""),
            "type": data.get("type", ""),
            "participants": participants,
            "price": price,
            "accessibility": str(data.get("accessibility", "")),
            "link": data.get("link", ""),
        }

        obj, created = Activity.objects.update_or_create(id=key, defaults=defaults)
        if created:
            added += 1
        else:
            skipped += 1

        if tp() - start > timeout:
            break

        if added > 0:
            cache.delete("activity_filter_choices")

    return {"added": added,
        "skipped": skipped,
        "errors": (errors),
        "timeout_reached": tp() - start > timeout,}
    