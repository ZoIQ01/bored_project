"""FilterSet definitions for activity listing queries."""

import django_filters

from activities.models import Activity


class ActivityFilterSet(django_filters.FilterSet):
    """Filter activities by exact fields plus activity name text search."""

    type = django_filters.CharFilter(field_name="type", lookup_expr="exact")
    participants = django_filters.NumberFilter(field_name="participants")
    price = django_filters.NumberFilter(field_name="price")
    accessibility = django_filters.CharFilter(field_name="accessibility", lookup_expr="exact")
    activity = django_filters.CharFilter(field_name="activity", lookup_expr="icontains")

    class Meta:
        model = Activity
        fields = ["type", "participants", "price", "accessibility", "activity"]
