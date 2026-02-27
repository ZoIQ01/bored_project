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

    accessibility = list(
        Activity.objects.order_by("accessibility")
        .values_list("accessibility", flat=True)
        .distinct()
    )

    data = {
        "types": types,
        "accessibility": accessibility,
    }

    cache.set(cache_key, data, CACHE_TIMEOUT)

    return data
