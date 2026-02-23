"""Activity detail page view definitions."""

from django.views.generic import DetailView

from activities.models import Activity


class ActivityDetailView(DetailView):
    """Render one activity detail page by primary key."""
    model = Activity
    template_name = "activities/activity_page.html"
    context_object_name = "activity"


activity_detail = ActivityDetailView.as_view()