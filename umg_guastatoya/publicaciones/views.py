from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from publicaciones.serializers import (
    ClasificacionSerializer, 
    PublicacionSerializer, 
    PublicacionDepthSerializer,
)
from publicaciones.models import (
    Clasificacion,
    Publicacion
)


class ClasificacionViewSet(ModelViewSet):
    serializer_class = ClasificacionSerializer
    queryset = Clasificacion.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PublicacionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        if 'clasificacion_id' in self.request.query_params:
            return Publicacion.objects.filter(clasificacion__pk=self.request.query_params['clasificacion_id']).order_by('-fecha_hora_creacion')
        return Publicacion.objects.all().order_by('-fecha_hora_creacion')
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PublicacionDepthSerializer
        return PublicacionSerializer

