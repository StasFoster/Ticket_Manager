from django import forms

from .models import Task, Company

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields=["name", "discription", "executor", "company"]

class CreateCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields=["name", "discription", "fieild_of_activity"]
