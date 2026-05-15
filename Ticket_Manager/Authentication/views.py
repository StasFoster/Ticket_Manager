from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import login, logout
from .models import MyUser

class CreateUserView(View):

    data = {
        "form":None,
        "flag":True,
    }

    def get(self, request):
        form = forms.MyUserCreateForm()
        self.data["form"] = form
        return render(request, "auth/index.html", self.data)
    def post(self, request):
        form = forms.MyUserCreateForm(data=request.POST)
        if form.is_valid():
            if MyUser.objects.filter(username=form.cleaned_data["username"]).exists():
                return redirect("auth")
            user = form.save()
            login(request, user)
            return redirect("main", page="main")
        return redirect("auth")

class AuthUserView(View):
    data = {
        "form":None,
        "flag":False,
    }

    def get(self, request):
        form = forms.MyUserAuthenticationForm()
        self.data["form"] = form
        return render(request, "auth/index.html", self.data)
    def post(self, request):
        form = forms.MyUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main", page="main")
        return redirect("login")