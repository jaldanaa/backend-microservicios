from django.contrib import admin
from evaluaciones.models import (
    Curso,
    Evaluacion,
    Pregunta,
    Respuesta,
    EvaluacionResuelta,
    RespuestaSeleccionada,
)

admin.site.register(Curso)
admin.site.register(Evaluacion)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(EvaluacionResuelta)
admin.site.register(RespuestaSeleccionada)