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


class TaskFilterForm(forms.Form):
    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        required=False,
        empty_label="All Task Types",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    is_completed = forms.ChoiceField(
        choices=(
            ("", "All Tasks"),
            ("False", "Incomplete Tasks"),
            ("True", "Completed Tasks"),
        ),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    deadline_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    deadline_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    assignee = forms.ModelChoiceField(
        queryset=Worker.objects.all(),
        required=False,
        empty_label="All Workers",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Search tasks..."})
    )


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
