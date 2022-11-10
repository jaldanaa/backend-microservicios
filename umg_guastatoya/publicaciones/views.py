from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView

from publicaciones.serializers import (
    ClasificacionSerializer, 
    PublicacionSerializer, 
    PublicacionDepthSerializer,
)
from publicaciones.models import (
    Clasificacion,
    Publicacion
)

from .filters import (
    PublicacionFilter
)

from .pagniations import (
    PublicacionPagination
)

from .permissions import (
    IsAdminOrPublisher
)


class ClasificacionViewSet(ModelViewSet):
    serializer_class = ClasificacionSerializer
    queryset = Clasificacion.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )


# Assume url for this view is /api/v1/companies/
class PublicacionListView(ListAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionDepthSerializer
    pagination_class = PublicacionPagination


class PublicacionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrPublisher)
    filterset_class = PublicacionFilter
    pagination_class = PublicacionPagination

    def get_queryset(self):
        if 'clasificacion_id' in self.request.query_params:
            return Publicacion.objects.filter(clasificacion__pk=self.request.query_params['clasificacion_id']).order_by('-fecha_hora_creacion')
        if 'limit' in self.request.query_params:
            return Publicacion.objects.all().order_by('-fecha_hora_creacion')[:int(self.request.query_params['limit'])]
        return Publicacion.objects.all().order_by('-fecha_hora_creacion')
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PublicacionDepthSerializer
        return PublicacionSerializer

