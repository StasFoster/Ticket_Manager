from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):

    class Role(models.IntegerChoices):
        employee = 1, "Cотрудник"
        director = 2, "Руководитель"
        help_director = 3, "Помошник руководителя"

    role = models.IntegerField("Роль", choices=Role)
    permission = models.JSONField(null=True)
    company = models.ForeignKey("Main.Company", verbose_name=("Компания"), on_delete=models.CASCADE, null=True)
