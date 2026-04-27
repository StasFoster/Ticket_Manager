from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView

from .forms import CreateTask, CreateCompany

def router(request, page):
    if not request.user.is_authenticated:
        return redirect("auth")
    elif page == "main":
        return render(request,"main/index.html")
    elif page == "tasks":
        return render(request,"main/tasks.html")
    elif page == "teams":
        return render(request,"main/teams.html")
    elif page == "setings":
        return render(request,"main/setings.html")
    
class CreateCompanyView(CreateView):
    form_class = CreateCompany
    template_name = ""
    success_url = 'tasks'

    def form_valid(self, form):
        super().form_valid(form)
        return redirect(self.success_url)
