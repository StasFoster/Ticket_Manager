from django.urls import path

from . import views

urlpatterns = [
    path("main/<str:page>/", views.router, name="main" ),
    path("main/createCompany/", views.CreateCompanyView.as_view(), name="createCompany" ),
]
