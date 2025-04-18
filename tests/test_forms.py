from django.test import TestCase
from django.utils import timezone
from datetime import date, timedelta

from task_app.forms import (
    TaskForm,
    TaskTypeForm,
)
from accounts.forms import (
    PositionForm,
    WorkerCreationForm,
    WorkerUpdateForm,
)
from task_app.models import Task, TaskType
from accounts.models import Worker, Position


class TaskFormTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.worker = Worker.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

    def test_task_form_valid_data(self):
        form_data = {
            "name": "Fix login bug",
            "description": "Users can't login using special characters",
            "deadline": date.today() + timedelta(days=3),
            "priority": "High",
            "task_type": self.task_type.pk,
            "assignees": [self.worker.pk],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_task_form_no_data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)
        
    def test_task_form_invalid_date(self):
        form_data = {
            "name": "Fix login bug",
            "description": "Users can't login using special characters",
            "deadline": "not-a-date",
            "priority": "High",
            "task_type": self.task_type.pk,
            "assignees": [self.worker.pk],
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("deadline", form.errors)


class PositionFormTest(TestCase):
    def test_position_form_valid_data(self):
        form_data = {"name": "Developer"}
        form = PositionForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_position_form_no_data(self):
        form = PositionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class TaskTypeFormTest(TestCase):
    def test_tasktype_form_valid_data(self):
        form_data = {"name": "Feature Development"}
        form = TaskTypeForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_tasktype_form_no_data(self):
        form = TaskTypeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class WorkerCreationFormTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Designer")
        
    def test_worker_creation_form_valid_data(self):
        form_data = {
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "email": "new@example.com",
            "position": self.position.pk,
            "password1": "complex_password123",
            "password2": "complex_password123",
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_worker_creation_form_password_mismatch(self):
        form_data = {
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "email": "new@example.com",
            "position": self.position.pk,
            "password1": "complex_password123",
            "password2": "different_password",
        }
        form = WorkerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


class WorkerUpdateFormTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testuser",
            password="testpassword123",
            first_name="Test",
            last_name="User",
            email="test@example.com",
        )
        
    def test_worker_update_form_valid_data(self):
        form_data = {
            "username": "updateduser",
            "first_name": "Updated",
            "last_name": "User",
            "email": "updated@example.com",
            "position": self.position.pk,
        }
        form = WorkerUpdateForm(data=form_data, instance=self.worker)
        self.assertTrue(form.is_valid())
        
    def test_worker_update_form_no_data(self):
        form = WorkerUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
