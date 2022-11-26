from django.urls import path, include
from rest_framework import routers
from inscripciones.views import (
    padres_representantesViewSet,
    alumnosViewSet,
    asignacionViewSet,
    notasViewSet
)

app_name = 'inscripciones'

router = routers.DefaultRouter()
router.register('representantes', padres_representantesViewSet, basename='representantes')
router.register('alumnos', alumnosViewSet, basename='alumnos')
router.register('asignaciones', asignacionViewSet, basename='asignaciones')
router.register('notas', notasViewSet, basename='notas')

urlpatterns = [
    path('', include(router.urls))
]