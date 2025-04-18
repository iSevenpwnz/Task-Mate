from django.urls import path

from task_app import views

app_name = 'task_app'

urlpatterns = [
    path(
        "", views.index,
        name="index"
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
        "tasks/<int:pk>/complete/", views.CompleteTaskView.as_view(), name="task-complete"
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
