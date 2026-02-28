"""Shared base class for activity list, filter, and sort pages."""

from django.conf import settings
from django.views.generic import ListView

from activities.filters import ActivityFilterSet
from activities.forms import ActivityFilterForm
from activities.models import Activity
from activities.services.activity_cache import get_activity_filter_choices


class BaseActivityListView(ListView):
    """Provide filtering, ordering hooks, and shared context for activity lists."""
    model = Activity
    template_name = "activities/activity_list.html"
    paginate_by = settings.ACTIVITIES_PER_PAGE
    valid_sort_fields = ["id", "type", "participants", "price", "accessibility", "activity"]

    def get_choices(self):
        """Return cached choice data used by filters and context."""
        if not hasattr(self, "_choices"):
            self._choices = get_activity_filter_choices()
        return self._choices

    def get_filter_form(self):
        """Build and cache the filter form bound to current query parameters."""
        if not hasattr(self, "_form"):
            choices = self.get_choices()
            self._form = ActivityFilterForm(
                self.request.GET or None,
                types=choices["types"],
                accessibility=choices["accessibility"],
            )
        return self._form

    def get_ordering_field(self):
        """Return validated ordering expression from query parameters."""
        sort_by = self.request.GET.get("sort_by", "id")
        if sort_by not in self.valid_sort_fields:
            sort_by = "id"

        order = self.request.GET.get("order", "asc")
        return f"-{sort_by}" if order == "desc" else sort_by

    def get_queryset(self):
        """Return activities filtered by form values and optional ordering."""
        queryset = Activity.objects.all()
        form = self.get_filter_form()

        if form.is_valid():
            filterset = ActivityFilterSet(
                data=form.cleaned_data,
                queryset=queryset,
            )
            queryset = filterset.qs

        ordering_field = self.get_ordering_field()
        if ordering_field:
            queryset = queryset.order_by(ordering_field)

        return queryset

    def get_context_data(self, **kwargs):
        """Add form and filter options to the template context."""
        context = super().get_context_data(**kwargs)
        choices = self.get_choices()

        context["types"] = choices["types"]
        context["accessibility_choices"] = choices["accessibility"]
        context["form"] = self.get_filter_form()
        return context
