"""Default activity table list view definitions."""

from activities.views.base_list_view import BaseActivityListView


class ActivitiesListView(BaseActivityListView):
    """Expose the default activity list page."""
    pass


activities_list = ActivitiesListView.as_view()
