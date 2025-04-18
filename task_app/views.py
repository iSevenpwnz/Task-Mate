from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q
from datetime import datetime

from .forms import (
    TaskForm,
    PositionForm,
    TaskTypeForm,
    WorkerCreationForm,
    WorkerUpdateForm,
    TaskFilterForm,
)
from .models import Task, Worker, Position, TaskType


def index(request):
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()
    num_positions = Position.objects.count()
    num_task_types = TaskType.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
        "num_positions": num_positions,
        "num_task_types": num_task_types,
    }

    return render(request, "task_app/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_app/task_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Task.objects.all().order_by("deadline")

        task_type_id = self.request.GET.get('task_type')
        is_completed = self.request.GET.get('is_completed')
        deadline_from = self.request.GET.get('deadline_from')
        deadline_to = self.request.GET.get('deadline_to')
        assignee_id = self.request.GET.get('assignee')
        search_query = self.request.GET.get('search_query')

        if task_type_id:
            queryset = queryset.filter(task_type_id=task_type_id)
        
        if is_completed:
            if is_completed == 'True':
                queryset = queryset.filter(is_completed=True)
            elif is_completed == 'False':
                queryset = queryset.filter(is_completed=False)
        
        if deadline_from:
            try:
                from_date = datetime.strptime(deadline_from, '%Y-%m-%d').date()
                queryset = queryset.filter(deadline__gte=from_date)
            except ValueError:
                pass
        
        if deadline_to:
            try:
                to_date = datetime.strptime(deadline_to, '%Y-%m-%d').date()
                queryset = queryset.filter(deadline__lte=to_date)
            except ValueError:
                pass
        
        if assignee_id:
            queryset = queryset.filter(assignee_id=assignee_id)
        
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.GET)
        context['current_filters'] = self.request.GET.dict()
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "task_app/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_app/task_form.html"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_app/task_form.html"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "task_app/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("task-detail", pk=pk)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect("index")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "task_app/position_list.html"


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    template_name = "task_app/position_form.html"
    success_url = reverse_lazy("position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm
    template_name = "task_app/position_form.html"
    success_url = reverse_lazy("position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "task_app/position_confirm_delete.html"
    success_url = reverse_lazy("position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "tasktype_list"
    template_name = "task_app/tasktype_list.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_app/tasktype_form.html"
    success_url = reverse_lazy("tasktype-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_app/tasktype_form.html"
    success_url = reverse_lazy("tasktype-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task_app/tasktype_confirm_delete.html"
    success_url = reverse_lazy("tasktype-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task_app/worker_list.html"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "task_app/worker_detail.html"


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "task_app/worker_form.html"
    success_url = reverse_lazy("login")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    template_name = "task_app/worker_form.html"

    def get_success_url(self):
        return reverse_lazy("worker-detail", kwargs={"pk": self.object.pk})


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    template_name = "task_app/worker_confirm_delete.html"
    success_url = reverse_lazy("worker-list")
