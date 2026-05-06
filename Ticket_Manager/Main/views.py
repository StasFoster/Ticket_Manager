from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

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
        
