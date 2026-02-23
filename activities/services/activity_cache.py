"""Caching helpers for activity filter option lists."""

from django.core.cache import cache
from activities.models import Activity, ActivityType


CACHE_TIMEOUT = 60 * 60


def get_activity_filter_choices():
    """Return distinct filter choices for activity list controls, cached by key."""
    cache_key = "activity_filter_choices"

    data = cache.get(cache_key)
    if data:
        return data

    types = [value for value, _ in ActivityType.choices]

    participants = list(
        Activity.objects.order_by("participants")
        .values_list("participants", flat=True)
        .distinct()
    )

    price = list(
        Activity.objects.order_by("price")
        .values_list("price", flat=True)
        .distinct()
    )

    accessibility = list(
        Activity.objects.order_by("accessibility")
        .values_list("accessibility", flat=True)
        .distinct()
    )

    data = {
        "types": types,
        "participants": participants,
        "price": price,
        "accessibility": accessibility,
    }

    cache.set(cache_key, data, CACHE_TIMEOUT)

    return data
