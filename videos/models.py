from django.db import models
from django.contrib import admin

# Create your models here.
class PopularVideo(models.Model):
    url = models.URLField(max_length=200)
    titulo = models.CharField(max_length=50)
    dsc = models.TextField()

    def __str__(self) -> str:
        return self.titulo

class Videos(models.Model):
    url = models.URLField(max_length=200)
    titulo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.titulo
