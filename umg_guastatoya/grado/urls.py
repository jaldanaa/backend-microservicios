from django.urls import path, include
from rest_framework import routers

from grado.views import (
    GradoViewSet,
    CursosViewSet,
    CursosList
)

app_name = 'grados'

router = routers.DefaultRouter()
router.register('grados', GradoViewSet, basename='grados')
router.register('cursos', CursosViewSet, basename='cursos')

urlpatterns = [    
    path('', include(router.urls))
]