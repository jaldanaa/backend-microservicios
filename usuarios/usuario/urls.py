from django.urls import path, include
from rest_framework import routers
from usuario.views import UsuarioViewset

app_name = 'usuario'

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewset, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
]