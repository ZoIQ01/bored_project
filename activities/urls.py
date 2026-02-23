"""URL patterns for activities app endpoints."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("activities/", views.activities_list, name="activities_list"),
    path("activities/import/", views.import_activities_view, name="import_activities_view"),
    path("activities/random/", views.random_activity, name="random_activity"),
    path("activities/<int:pk>/", views.activity_detail, name="activity_detail"),
]