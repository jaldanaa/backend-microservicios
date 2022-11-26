from rest_framework import serializers
from inscripciones.models import padres_representantes, alumnos, asignacion, notas


class Padres_representantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = padres_representantes
        fields = '__all__'


class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = alumnos
        fields = '__all__'

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = asignacion
        fields = '__all__'

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = notas
        fields = '__all__'
