from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

# Replace default User admin with a fully configured one
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    """Admin for adding, editing, and deleting users."""

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    list_per_page = 25

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
            'description': 'Staff can log in to admin. Superuser has all permissions.',
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Personal info (optional)', {
            'classes': ('wide', 'collapse'),
            'fields': ('first_name', 'last_name'),
        }),
        ('Permissions', {
            'classes': ('wide', 'collapse'),
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.unregister(Group)


@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    """Admin for managing user groups."""
    search_fields = ('name',)
    filter_horizontal = ('permissions',)
