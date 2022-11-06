from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.score)


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    score = models.ForeignKey(
        Rate, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
