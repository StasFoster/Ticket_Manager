from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views import View

from django.http import JsonResponse

import json

from django.urls import reverse_lazy

from .forms import CreateTask, CreateCompany
from .models import Task, Company

def router(request, page):
    if not request.user.is_authenticated:
        return redirect("auth")
    elif page == "main":
        return render(request,"main/index.html")
    elif page == "tasks":
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
        
class ListTaskView(ListView):
    model = Task
    template_name = "main/tasks.html"

class ListTeamsView(ListView):
    model = Company
    template_name = "main/teams.html"

class UpdateStatus(View):
    def post(self, request):
        data = json.loads(request.body)
        id = data.get("id")
        status = data.get("value")
        task = Task.objects.get(id=id)
        task.status = int(status)
        task.save()
        return JsonResponse({})