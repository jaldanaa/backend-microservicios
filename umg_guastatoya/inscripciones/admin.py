from django.contrib import admin
from inscripciones.models import(
    padres_representantes,
    alumnos,
    asignacion
)

admin.site.register(padres_representantes)
admin.site.register(alumnos)
admin.site.register(asignacion)
# Register your models here.
