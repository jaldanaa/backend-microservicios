from rest_framework import serializers
from publicaciones.models import Clasificacion, Publicacion


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'


class PublicacionDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'
        depth = 1


