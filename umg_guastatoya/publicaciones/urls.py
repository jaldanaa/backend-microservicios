from django.urls import path, include
from rest_framework import routers

from publicaciones.views import (
    ClasificacionViewSet,
    PublicacionViewSet,
    PublicacionListView
)

app_name = 'publicaciones'

router = routers.DefaultRouter()
router.register('clasificaciones', ClasificacionViewSet, basename='clasificaciones')
router.register('publicaciones', PublicacionViewSet, basename='publicaciones')

urlpatterns = [
    path('', include(router.urls)),
    path('publicaciones-paginadas/', PublicacionListView.as_view(), name='publicaciones-paginadas')
]