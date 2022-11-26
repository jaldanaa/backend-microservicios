from rest_framework import serializers
from grado.models import (
    Grado,
    Cursos
)


class GradoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'
