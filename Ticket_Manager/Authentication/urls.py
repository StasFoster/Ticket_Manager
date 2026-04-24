from django.urls import path
from . import views
urlpatterns = [
    path('auth/', views.CreateUserView.as_view(), name="auth"),
    path('login/', views.AuthUserView.as_view(), name="login"),
]
