from django.urls import path, include
from rest_framework import routers

from publicaciones.views import (
    ClasificacionViewSet,
    PublicacionViewSet
)

app_name = 'publicaciones'

router = routers.DefaultRouter()
router.register('clasificaciones', ClasificacionViewSet, basename='clasificaciones')
router.register('publicaciones', PublicacionViewSet, basename='publicaciones')

urlpatterns = [
    path('', include(router.urls)),
]