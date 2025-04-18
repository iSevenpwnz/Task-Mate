from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login"
    ),
    path(
        "logout/",
        views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        "register/",
        views.WorkerCreateView.as_view(),
        name="register"
    ),
    path(
        "workers/",
        views.WorkerListView.as_view(),
        name="worker-list"
    ),
    path(
        "workers/<int:pk>/",
        views.WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/<int:pk>/update/",
        views.WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/",
        views.WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
    path(
        "positions/",
        views.PositionListView.as_view(),
        name="position-list"
    ),
    path(
        "positions/create/",
        views.PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "positions/<int:pk>/update/",
        views.PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "positions/<int:pk>/delete/",
        views.PositionDeleteView.as_view(),
        name="position-delete"
    ),
]
