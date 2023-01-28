from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("email", "first_name", "last_name", "phone")
    list_display = ("get_full_name", "email", "is_active")
    list_filter = ("is_active", "is_superuser")
    ordering = ("email",)
    readonly_fields = ("date_joined",)
    fieldsets = (
        ('Info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}), # TODO: add sites that the user have access to
    )


admin.site.unregister(Group)

