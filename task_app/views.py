from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView
from django.db.models import Q
from datetime import datetime

from accounts.models import Worker, Position
from task_app.forms import (
    TaskForm,
    TaskTypeForm,
    TaskFilterForm,
)
from task_app.models import Task, TaskType


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
    success_url = reverse_lazy("task_app:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_app/task_form.html"
    success_url = reverse_lazy("task_app:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "task_app/task_confirm_delete.html"
    success_url = reverse_lazy("task_app:task-list")


class CompleteTaskView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("task_app:task-detail", kwargs={"pk": kwargs.get("pk")})
    
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        task.is_completed = True
        task.save()
        return super().get(request, *args, **kwargs)


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "tasktype_list"
    template_name = "task_app/tasktype_list.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_app/tasktype_form.html"
    success_url = reverse_lazy("task_app:tasktype-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_app/tasktype_form.html"
    success_url = reverse_lazy("task_app:tasktype-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task_app/tasktype_confirm_delete.html"
    success_url = reverse_lazy("task_app:tasktype-list")
