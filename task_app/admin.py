from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Worker, Task, Position, TaskType


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


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "deadline",
        "is_completed",
        "priority",
        "task_type",
    ]
    list_filter = ["is_completed", "priority", "task_type"]
    search_fields = ["name", "description"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
