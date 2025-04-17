from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import date, timedelta

from task_app.models import Task, Worker, Position, TaskType


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Створення тестових даних
        Position.objects.create(name="Developer")
        TaskType.objects.create(name="Bug Fix")
        Worker.objects.create(
            username="admin_user",
            password="testpassword123",
            is_staff=True,
            is_superuser=True
        )
        task_type = TaskType.objects.get(name="Bug Fix")
        Task.objects.create(
            name="Test Task",
            description="Description",
            deadline=date.today() + timedelta(days=7),
            priority="Medium",
            task_type=task_type
        )

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_app/index.html")
        self.assertEqual(response.context["num_tasks"], 1)
        self.assertEqual(response.context["num_workers"], 1)
        self.assertEqual(response.context["num_positions"], 1)
        self.assertEqual(response.context["num_task_types"], 1)


class TaskViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Створення користувача для авторизації
        self.user = Worker.objects.create_user(
            username="testuser",
            password="testpassword123"
        )
        
        # Створення тестових даних
        task_type = TaskType.objects.create(name="Feature")
        self.task = Task.objects.create(
            name="Implement login",
            description="Create login functionality",
            deadline=date.today() + timedelta(days=14),
            priority="High",
            task_type=task_type
        )
        self.task.assignees.add(self.user)
        
        # Вхід користувача
        self.client.login(username="testuser", password="testpassword123")

    def test_task_list_view(self):
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_app/task_list.html")
        self.assertContains(response, "Implement login")
        
    def test_task_detail_view(self):
        response = self.client.get(reverse("task-detail", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_app/task_detail.html")
        self.assertEqual(response.context["task"], self.task)
        
    def test_task_complete(self):
        self.assertFalse(self.task.is_completed)
        response = self.client.get(reverse("task-complete", kwargs={"pk": self.task.pk}))
        self.assertRedirects(response, reverse("task-detail", kwargs={"pk": self.task.pk}))
        # Перевірка, що завдання позначено як виконане
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)


class WorkerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Створення користувача для авторизації
        self.admin = Worker.objects.create_superuser(
            username="admin",
            password="admin123",
            email="admin@example.com"
        )
        
        # Створення тестових даних
        self.position = Position.objects.create(name="QA Engineer")
        self.worker = Worker.objects.create_user(
            username="worker1",
            password="worker123",
            first_name="Test",
            last_name="Worker",
            email="worker@example.com",
            position=self.position
        )
        
        # Вхід адміністратора
        self.client.login(username="admin", password="admin123")

    def test_worker_list_view(self):
        response = self.client.get(reverse("worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_app/worker_list.html")
        self.assertContains(response, "worker1")
        
    def test_worker_detail_view(self):
        response = self.client.get(reverse("worker-detail", kwargs={"pk": self.worker.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_app/worker_detail.html")
        self.assertEqual(response.context["worker"], self.worker)


class PositionAndTaskTypeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Створення користувача для авторизації
        self.admin = Worker.objects.create_superuser(
            username="admin",
            password="admin123"
        )
        
        # Створення тестових даних
        self.position = Position.objects.create(name="Project Manager")
        self.task_type = TaskType.objects.create(name="Documentation")
        
        # Вхід адміністратора
        self.client.login(username="admin", password="admin123")

    def test_position_list_view(self):
        response = self.client.get(reverse("position-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_app/position_list.html")
        self.assertContains(response, "Project Manager")
        
    def test_tasktype_list_view(self):
        response = self.client.get(reverse("tasktype-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_app/tasktype_list.html")
        self.assertContains(response, "Documentation")
