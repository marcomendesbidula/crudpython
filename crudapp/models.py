from django.db import models

# Create your models here.
class Carros(models.Model):
    objects = None
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()