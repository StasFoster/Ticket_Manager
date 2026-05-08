from django.urls import path

from . import views

urlpatterns = [
    path("main/<str:page>/", views.router, name="main" ),
    path("createCompany/", views.CreateCompanyView.as_view(), name="createCompany" ),
    path("createTask/", views.CreateTaskView.as_view(), name="createTask"),
    path("tasks/", views.ListTaskView.as_view(), name="tasks"),
    path("teams/", views.ListTeamsView.as_view(), name="teams"),
    path("api/task/status/", views.UpdateStatus.as_view(), name="statusUpdate" ),
]
