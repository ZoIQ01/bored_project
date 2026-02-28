from .base_list_view import BaseActivityListView


class ActivitiesListView(BaseActivityListView):
    pass


activities_list = ActivitiesListView.as_view()