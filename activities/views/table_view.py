from django_filters.views import FilterView
from activities.filters import ActivityFilterSet
from activities.models import Activity


class ActivitiesListView(FilterView):
    model = Activity
    filterset_class = ActivityFilterSet
    template_name = "activities/activity_list.html"
    paginate_by = 20