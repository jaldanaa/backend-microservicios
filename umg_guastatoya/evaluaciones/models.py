from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nombre = models.CharField(max_length=250)


class Evaluacion(models.Model):
    titulo = models.CharField(max_length=250)

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='curso_evaluaciones')
    catedratico = models.ForeignKey(User, on_delete=models.CASCADE, related_name='catedratico_evaluaciones')


class Pregunta(models.Model):
    titulo = models.CharField(max_length=500)
    
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='preguntas')


class Respuesta(models.Model):
    titulo = models.CharField(max_length=500)
    correcto = models.BooleanField()
    
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')


class EvaluacionResuelta(models.Model):
    ponderacion = models.IntegerField(default=0)
    fecha_hora_creacion = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(null=True, blank=True)
    
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='evaluacion_evaluaciones_resueltas')
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estudiante_evaluaciones_resueltas')


class RespuestaSeleccionada(models.Model):
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, related_name='respuesta_respuestas_seleccionadas')
    evaluacion_resuelta = models.ForeignKey(EvaluacionResuelta, on_delete=models.CASCADE, related_name='evaluacion_resuelta_respuestas_seleccionadas')
