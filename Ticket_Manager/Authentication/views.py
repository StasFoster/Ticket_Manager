from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import login, logout

class CreateUserView(View):

    data = {
        "form":None,
        "flag":None,
    }

    def get(self, request):
        form = forms.MyUserCreateForm()
        self.data["form"] = form
        return render(request, "auth/index.html", self.data)
    def post(self, request):
        form = forms.MyUserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main")
        return redirect("auth")

class AuthUserView(View):
    data = {
        "form":None,
        "flag":None,
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
            return redirect("main")
        return redirect("login")