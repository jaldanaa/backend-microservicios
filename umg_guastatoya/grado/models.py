from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Grado(models.Model):
    grado = models.CharField(max_length=100)
    nivel_educativo = models.CharField(max_length=200)

class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=150)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name='grado_cursos')
    horario = models.CharField(max_length=25)

