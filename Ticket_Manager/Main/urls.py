from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tasks", views.TaskView)


urlpatterns = [
    path("main/<str:page>/", views.router, name="main" ),
    path("createCompany/", views.CreateCompanyView.as_view(), name="createCompany" ),
    path("createTask/", views.CreateTaskView.as_view(), name="createTask"),
    path("teams/", views.ListTeamsView.as_view(), name="teams"),
] + router.urls
