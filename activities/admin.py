"""Admin registration for activity models."""

from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for browsing and searching activities."""
    list_display = ['id', 'activity', 'type', 'participants', 'price', 'accessibility']
    list_filter = ['type', 'participants']
    search_fields = ['activity', 'type']
    ordering = ['-id']
    list_per_page = 25

