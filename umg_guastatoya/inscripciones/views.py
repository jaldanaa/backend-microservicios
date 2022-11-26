from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from inscripciones.serializers import (
    Padres_representantesSerializers,
    AlumnosSerializer,
    AsignacionSerializer,
    NotasSerializer
)
from grado.models import Cursos
from inscripciones.models import(
    padres_representantes,
    alumnos,
    asignacion,
    notas
)

class padres_representantesViewSet(ModelViewSet):
    serializer_class = Padres_representantesSerializers
    queryset = padres_representantes.objects.all()

class alumnosViewSet(ModelViewSet):
    serializer_class = AlumnosSerializer
    def get_queryset(self):
        if 'grado_id' in self.request.query_params:
            return alumnosGrado(self.request.query_params['grado_id'],self.request.query_params['v_ciclo'])      
        return alumnos.objects.all()

class asignacionViewSet(ModelViewSet):
    serializer_class = AsignacionSerializer
    queryset = asignacion.objects.all()

def alumnosGrado(gradiId, v_ciclo):
    asignaciones = asignacion.objects.values('alumno').filter(grado__pk=gradiId, ciclo = v_ciclo)  
    return alumnos.objects.filter(id__in=asignaciones)

class notasViewSet(ModelViewSet):
    serializer_class = NotasSerializer
    def get_queryset(self):
        if 'alumno_id' in self.request.query_params:
            return notas.objects.filter(alumno__pk=self.request.query_params['alumno_id'], ciclo = self.request.query_params['v_ciclo']).order_by('curso')
        return notas.objects.all()
