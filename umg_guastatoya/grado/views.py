from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from grado.serializers import GradoSerializers
from grado.serializers import CursoSerializer
from grado.models import(
    Grado, Cursos
)

class GradoViewSet(ModelViewSet):
    serializer_class = GradoSerializers
    queryset = Grado.objects.all()

class GradoList(ListAPIView):
    serializer_class = GradoSerializers
    queryset = Grado.objects.all()

class CursosViewSet(ModelViewSet):
    serializer_class = CursoSerializer
    def get_queryset(self):
        if 'grado_id' in self.request.query_params:
            return Cursos.objects.filter(grado__pk=self.request.query_params['grado_id'])        
        return Cursos.objects.all()

class CursosList(ListAPIView):
    serializer_class = CursoSerializer
    def get_queryset(self):
        if 'grado_id' in self.request.query_params:
            return Cursos.objects.filter(grado__pk=self.request.query_params['grado_id'])        
        return Cursos.objects.all()
