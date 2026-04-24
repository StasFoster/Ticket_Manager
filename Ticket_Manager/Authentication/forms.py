from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import MyUser

class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username", "first_name","last_name", "email","role", "password1","password2"]

class MyUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(max_length=50, required=False)

