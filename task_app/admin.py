from django.contrib import admin

from task_app.models import Task, TaskType


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


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
