from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView

from accounts.forms import WorkerCreationForm, WorkerUpdateForm, PositionForm
from accounts.models import Worker, Position


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "accounts/worker_form.html"
    success_url = reverse_lazy("accounts:login")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "accounts/worker_detail.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    template_name = "accounts/worker_form.html"

    def get_success_url(self):
        return reverse_lazy("accounts:worker-detail", kwargs={"pk": self.object.pk})


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    template_name = "accounts/worker_confirm_delete.html"
    success_url = reverse_lazy("accounts:worker-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "accounts/worker_list.html"


class LogoutView(RedirectView):
    url = reverse_lazy("task_app:index")

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return super().get(request, *args, **kwargs)


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "accounts/position_list.html"


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    template_name = "accounts/position_form.html"
    success_url = reverse_lazy("accounts:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm
    template_name = "accounts/position_form.html"
    success_url = reverse_lazy("accounts:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "accounts/position_confirm_delete.html"
    success_url = reverse_lazy("accounts:position-list")
