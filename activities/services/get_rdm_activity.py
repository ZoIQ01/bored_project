"""Helpers for selecting a random activity from storage."""

import random
from activities.models import Activity    


def get_random_activity(queryset=None):
    """Return one random activity from a queryset, or None when empty."""
    qs = queryset if queryset is not None else Activity.objects.all()
    count = qs.count()
    if count == 0:
        return None
    random_index = random.randint(0, count - 1)
    return qs[random_index]