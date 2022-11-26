from django.db import models
from grado.models import (Grado, Cursos)

class padres_representantes(models.Model):
    nombres = models.CharField(max_length=200)    
    apellidos = models.CharField(max_length=200)
    dpi = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=8)
    sexo = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=60)
    parentesco_alumno = models.CharField(max_length=50)
    
class alumnos(models.Model):
    nombres = models.CharField(max_length=200)    
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateTimeField()
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=200)      
    nacionalidad = models.CharField(max_length=200)  
    sexo = models.CharField(max_length=20)
    partida_nacimiento = models.CharField(max_length=200)
    padre_representantes = models.ForeignKey(padres_representantes, on_delete=models.CASCADE, related_name='alumno_representante')

class asignacion(models.Model):
    alumno = models.ForeignKey(alumnos, on_delete=models.CASCADE, related_name='alumno_asignado')
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name='grado_asignado')
    ciclo = models.CharField(max_length=4)

class notas(models.Model):
    nota = models.CharField(max_length=3)
    alumno =  models.ForeignKey(alumnos, on_delete=models.CASCADE, related_name='alumno_nota')
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, related_name='cursos_nota')
    ciclo = models.CharField(max_length=4)