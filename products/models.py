from django.db import models
from django.db.models import Avg

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    @property
    def average_score(self):
        return self.score.aggregate(Avg('score'))['score_avg']
