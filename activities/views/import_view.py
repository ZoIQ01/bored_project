"""Views for importing activities from the external API."""

from django.urls import reverse_lazy
from django.views.generic import FormView

from activities.forms import ImportForm
from activities.models import Activity
from activities.services.import_from_api import import_activities


class ImportActivitiesView(FormView):
    """Handle activity import form submission and import summary details."""

    template_name = "activities/import.html"
    form_class = ImportForm
    success_url = reverse_lazy("import_activities_view")
    session_key = "import_result"

    def form_valid(self, form):
        """Import requested number of activities and store result in session."""
        count = form.cleaned_data["count"]
        result = import_activities(count, return_meta=True)
        if isinstance(result, tuple) and len(result) == 3:
            added, skipped, meta = result
        else:
            added, skipped = result
            meta = {
                "requested": count,
                "attempted": (added or 0) + (skipped or 0),
                "timeout_seconds": None,
                "timeout_reached": False,
            }
        self.request.session[self.session_key] = {
            "added": added,
            "skipped": skipped,
            "count": count,
            "attempted": meta.get("attempted"),
            "timeout_reached": meta.get("timeout_reached"),
            "timeout_seconds": meta.get("timeout_seconds"),
        }
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Add import result summary and total activity count to context."""
        context = super().get_context_data(**kwargs)
        result = self.request.session.pop(self.session_key, None)

        context["added"] = result.get("added") if result else None
        context["skipped"] = result.get("skipped") if result else None
        context["count"] = result.get("count") if result else None
        context["attempted"] = result.get("attempted") if result else None
        context["timeout_reached"] = result.get("timeout_reached") if result else None
        context["timeout_seconds"] = result.get("timeout_seconds") if result else None
        context["total"] = Activity.objects.count()

        return context


import_activities_view = ImportActivitiesView.as_view()
