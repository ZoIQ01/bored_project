import django_filters 
from activities.models import Activity, ActivityType


class ActivityFilterSet(django_filters.FilterSet):
    """Filter activities by exact fields plus activity name text search."""

    type = django_filters.ChoiceFilter(
        field_name="type",
        choices=ActivityType.choices,
        empty_label="Any"
    )
    participants = django_filters.NumberFilter(field_name="participants")
    price = django_filters.NumberFilter(field_name="price")
    accessibility = django_filters.ChoiceFilter(
        field_name="accessibility",
        empty_label="Any"
    )
    activity = django_filters.CharFilter(
        field_name="activity",
        lookup_expr="icontains",
        label="Activity name"
    )

    class Meta:
        model = Activity
        fields = ["type", "participants", "price", "accessibility", "activity"]