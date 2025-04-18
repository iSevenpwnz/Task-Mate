from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Worker, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "position",
    ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
