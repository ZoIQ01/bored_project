"""Views for showing one random activity."""

from django.views.generic import TemplateView

from activities.services.get_rdm_activity import get_random_activity


class RandomActivityView(TemplateView):
    """Render one random activity or an empty-state message."""

    template_name = "activities/random_activity.html"

    def get_context_data(self, **kwargs):
        """Add random activity data to template context."""
        context = super().get_context_data(**kwargs)
        activity = get_random_activity()
        if activity:
            context["activity"] = activity
        else:
            context["no_activities"] = True
        return context


random_activity = RandomActivityView.as_view()