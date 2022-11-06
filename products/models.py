from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
