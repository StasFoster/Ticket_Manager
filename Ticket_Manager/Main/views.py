from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views import View

from django.http import JsonResponse

import json

from django.urls import reverse_lazy

from django.db.models import QuerySet

from .forms import CreateTask, CreateCompany
from .models import Task, Company
from .serializers import TaskSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

def router(request, page):
    if not request.user.is_authenticated:
        return redirect("auth")
    elif page == "main":
        return render(request,"main/index.html")
    elif page == "task-list":
        return redirect("tasks")
    elif page == "teams":
        return redirect("teams")
    elif page == "setings":
        return render(request,"main/setings.html")
    return render(request,"main/index.html")
    


class CreateCompanyView(CreateView):
        form_class = CreateCompany
        template_name = "main/createCompany.html"
        success_url = reverse_lazy('main', kwargs = {"page" :'tasks'})

        def form_valid(self, form):
            company = form.save(commit=False)
            company.director = self.request.user
            company.save()
            return super().form_valid(form)
        
class CreateTaskView(CreateView):
    form_class = CreateTask
    template_name = "main/createCompany.html"
    success_url = reverse_lazy('main', kwargs = {"page" :'tasks'})     

class ListTeamsView(ListView):
    model = Company
    template_name = "main/teams.html"
    
class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role == 1:
            list_tasks = user.executor.all()
            return render(request, "main/tasks.html",
                {
                    "message":list_tasks
                }
            )
        elif user.role == 2:
            list_company = user.director_company.all()
            q1 = Task.objects.none()
            for i in list_company:
                list_task = i.company.all()
                q1 = q1.union(list_task)
            for j in q1:
                print(j.name)
            return render(request, "main/tasks.html",{
                "message":q1
            })

            


    
    