from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path(
        "", views.index,
        name="index"
    ),

    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login"
    ),
    path(
        "accounts/logout/", views.logout_view, name="logout"
    ),
    path(
        "accounts/register/", views.WorkerCreateView.as_view(),
        name="register"
    ),

    path(
        "tasks/", views.TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/<int:pk>/", views.TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/create/", views.TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/", views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/", views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/complete/", views.complete_task, name="task-complete"
    ),

    path(
        "workers/", views.WorkerListView.as_view(),
        name="worker-list"
    ),
    path(
        "workers/<int:pk>/", views.WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/<int:pk>/update/", views.WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/", views.WorkerDeleteView.as_view(),
        name="worker-delete"
    ),

    path(
        "positions/", views.PositionListView.as_view(),
        name="position-list"
    ),
    path(
        "positions/create/", views.PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "positions/<int:pk>/update/", views.PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "positions/<int:pk>/delete/", views.PositionDeleteView.as_view(),
        name="position-delete"
    ),

    path(
        "tasktypes/", views.TaskTypeListView.as_view(),
        name="tasktype-list"
    ),
    path(
        "tasktypes/create/", views.TaskTypeCreateView.as_view(),
        name="tasktype-create"
    ),
    path(
        "tasktypes/<int:pk>/update/", views.TaskTypeUpdateView.as_view(),
        name="tasktype-update"
    ),
    path(
        "tasktypes/<int:pk>/delete/", views.TaskTypeDeleteView.as_view(),
        name="tasktype-delete"
    ),
]
