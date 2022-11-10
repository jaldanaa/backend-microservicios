from django_filters import rest_framework as filters, DateFromToRangeFilter
from .models import Publicacion

class PublicacionFilter(filters.FilterSet):
  class Meta:
    model = Publicacion
    fields = {
      "titulo": ["icontains"],
    }
