from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from usuario import serializer.usuarioSerializer


class UsuarioViewset(ModelViewSet):
    serializer_class = usuarioSerializer
    queryset = User.objects.all()
