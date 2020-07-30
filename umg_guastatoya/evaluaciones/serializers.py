from rest_framework import serializers
from evaluaciones.models import (
    Curso,
    Evaluacion,
    Pregunta,
    Respuesta,
    EvaluacionResuelta,
    RespuestaSeleccionada
)

from users.serializers import UserProfileSerializer


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'


class PreguntaSerializer(serializers.ModelSerializer):
    respuestas = RespuestaSerializer(many=True)
    class Meta:
        model = Pregunta
        fields = '__all__'


class EvaluacionSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True)
    catedratico = UserProfileSerializer()
    curso = CursoSerializer()
    class Meta:
        model = Evaluacion
        fields = '__all__'


class RespuestaSeleccionadaSerializer(serializers.ModelSerializer):
    respuesta = RespuestaSerializer()
    class Meta:
        model = RespuestaSeleccionada
        fields = '__all__'


class EvaluacionResueltaSerializer(serializers.ModelSerializer):
    evaluacion = EvaluacionSerializer()
    estudiante = UserProfileSerializer()
    evaluacion_resuelta_respuestas_seleccionadas = RespuestaSeleccionadaSerializer(many=True)
    class Meta:
        model = EvaluacionResuelta
        fields = '__all__'
