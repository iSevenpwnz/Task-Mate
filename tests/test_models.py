from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import date, timedelta

from task_app.models import Task, TaskType
from accounts.models import Worker, Position


class PositionModelTest(TestCase):
    def setUp(self):
        Position.objects.create(name="Developer")

    def test_position_name(self):
        developer = Position.objects.get(name="Developer")
        self.assertEqual(str(developer), "Developer")


class TaskTypeModelTest(TestCase):
    def setUp(self):
        TaskType.objects.create(name="Bug Fix")

    def test_tasktype_name(self):
        bug_fix = TaskType.objects.get(name="Bug Fix")
        self.assertEqual(str(bug_fix), "Bug Fix")


class WorkerModelTest(TestCase):
    def setUp(self):
        position = Position.objects.create(name="Designer")
        Worker.objects.create(
            username="tester",
            first_name="Test",
            last_name="User",
            email="test@example.com",
            position=position,
        )

    def test_worker_str_representation(self):
        worker = Worker.objects.get(username="tester")
        self.assertEqual(str(worker), "Test User (tester)")
        
    def test_worker_position(self):
        worker = Worker.objects.get(username="tester")
        self.assertEqual(worker.position.name, "Designer")


class TaskModelTest(TestCase):
    def setUp(self):
        task_type = TaskType.objects.create(name="Feature Development")
        self.worker = Worker.objects.create(
            username="developer",
            first_name="Dev",
            last_name="User",
        )
        self.task = Task.objects.create(
            name="Create login page",
            description="Implement a secure login page with validation",
            deadline=date.today() + timedelta(days=7),
            is_completed=False,
            priority="High",
            task_type=task_type,
        )
        self.task.assignees.add(self.worker)

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), "Create login page")
        
    def test_task_priority(self):
        self.assertEqual(self.task.priority, "High")
        
    def test_task_deadline(self):
        self.assertEqual(self.task.deadline, date.today() + timedelta(days=7))
        
    def test_task_assignees(self):
        self.assertEqual(self.task.assignees.count(), 1)
        self.assertEqual(self.task.assignees.first().username, "developer")
        
    def test_task_completion(self):
        self.assertFalse(self.task.is_completed)
        self.task.is_completed = True
        self.task.save()
        self.assertTrue(Task.objects.get(pk=self.task.pk).is_completed)
