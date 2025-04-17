from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Medium"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks"
    )

    def __str__(self):
        return self.name
