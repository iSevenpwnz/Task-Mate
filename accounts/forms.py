from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Worker, Position


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


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ["name"]
