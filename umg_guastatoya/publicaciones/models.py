from django.db import models
from django.contrib.auth.models import User


class Clasificacion(models.Model):
    nombre = models.CharField(max_length=150)


class Publicacion(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='media/imagenes/', null=True, blank=True)
    fecha_hora_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor_publicaciones')
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, related_name='clasificacion_publicaciones')
    