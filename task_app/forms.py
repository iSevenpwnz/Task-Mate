from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Task, Worker, Position, TaskType


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees",
        ]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
            "assignees": forms.SelectMultiple(attrs={"class": "form-select"}),
        }


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ["name"]


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ["name"]


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
            "password1",
            "password2",
        ]


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
        ]
