"""Home page view for activities app."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
   """Render the activities home page."""

   template_name = "activities/home.html"


home = HomeView.as_view()