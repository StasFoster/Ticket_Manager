from django.db import models

class Company(models.Model):

    class Fieild_of_activity(models.TextChoices):
        it = "it", "IT"
        marketing = "marketing", "Маркетинг"
        production = "production", "Производство"

    name = models.CharField("Имя", max_length=50)
    discription = models.CharField("Описание", max_length=500, null=True, blank=True)
    fieild_of_activity = models.CharField("Сфера деятельности", max_length=50, choices=Fieild_of_activity)
    director = models.ForeignKey("Authentication.MyUser", verbose_name="Директор", on_delete=models.CASCADE, related_name="director_company")

    def __str__(self):
        return self.name

class Task(models.Model):

    class Status(models.IntegerChoices):
        new = 1, "Новая"
        accepted = 2, "Принята"
        review = 3, "На проверке"
        end = 4, "Завершена"
        postponed = 5, "Отложена"
        overdue = 6, "Просрочена"
        returned = 7, "Возвращена"


    name = models.CharField("Имя", max_length=50)
    discription = models.CharField("Описание", max_length=500, null=True, blank=True)
    executor = models.ForeignKey("Authentication.MyUser", verbose_name="Исполнитель", on_delete=models.CASCADE, null=True, blank=True, related_name="executor")
    company = models.ForeignKey("Main.Company", verbose_name="Компания", on_delete=models.CASCADE, related_name="company")
    status = models.IntegerField("Статус", choices=Status, default=1)