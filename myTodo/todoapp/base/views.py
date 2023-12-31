from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class CustomLoginView(LoginView):
    model = Task
    fiels = '__all__'
    redirect_authenticated_user = True
    template_name = 'base/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')



class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_users = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form: Any) -> HttpResponse:
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)



class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["color"] = "red"     ## It helps us pass more value than just the queried value.
        context["tasks"] = context["tasks"].filter(user = self.request.user)  ## Filter the tasks based on user and output the data
        context["count"] = context["tasks"].filter(complete = False).count()

        search_input = self.request.GET.get('Search') or ''
        print(search_input)
        if search_input:
            context["tasks"] = context["tasks"].filter(
                title__icontains = search_input)
            
        context["search_input"] = search_input
        return context



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"



class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = '__all__'  # Before form_valid
    fields = ["title", "desc", "complete"]
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_create.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)



class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "desc", "complete"]
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_create.html'



class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

