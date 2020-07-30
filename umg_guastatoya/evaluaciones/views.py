from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from evaluaciones.serializers import EvaluacionSerializer, CursoSerializer, EvaluacionResueltaSerializer
from evaluaciones.models import (
    Evaluacion,
    Pregunta,
    Respuesta,
    Curso,
    EvaluacionResuelta,
    RespuestaSeleccionada,
)
from django.contrib.auth.models import User


class CursoViewSet(ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    permission_classes = (IsAuthenticated, )


class EvaluacionList(ListAPIView):
    serializer_class = EvaluacionSerializer
    queryset = Evaluacion.objects.all()
    permission_classes = (IsAuthenticated, )


class EvaluacionRetrieve(RetrieveAPIView):
    serializer_class = EvaluacionSerializer
    queryset = Evaluacion.objects.all()
    permission_classes = (IsAuthenticated, )


class CreateEvaluacionAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        evaluacion_data = request.data
        preguntas = request.data['preguntas']

        # Get user object
        catedratico = User.objects.get(pk=evaluacion_data['catedratico'])
        # Get curso object
        curso = Curso.objects.get(pk=evaluacion_data['curso'])
        # Create evaluacion object
        evaluacion = Evaluacion.objects.create(
            titulo = evaluacion_data['titulo'],
            curso = curso,
            catedratico = catedratico
        )

        # Iterar sobre las preguntas para crear cada uno y luego sus respuestas
        for pregunta in preguntas:
            # Create pregunta object
            pregunta_object = Pregunta.objects.create(
                titulo = pregunta['titulo'],
                evaluacion = evaluacion
            )
            for respuesta in pregunta['respuestas']:
                Respuesta.objects.create(
                    titulo = respuesta['titulo'],
                    correcto = respuesta['correcto'],
                    pregunta = pregunta_object
                )
        serializer = EvaluacionSerializer(evaluacion)
        return Response(serializer.data)


class UpdateEvaluacionAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        evaluacion_data = request.data
        preguntas = request.data['preguntas']

        # Get curso object
        curso = Curso.objects.get(pk=evaluacion_data['curso'])
        # Create evaluacion object
        evaluacion = Evaluacion.objects.get(pk=evaluacion_data['id'])

        evaluacion.curso = curso
        evaluacion.titulo = evaluacion_data['titulo']
        evaluacion.save()
        # Iterar sobre las preguntas para modificar cada uno y luego sus respuestas
        for pregunta in preguntas:
            # Get pregunta object
            pregunta_object = Pregunta.objects.get(pk=pregunta['id'])
            pregunta_object.titulo = pregunta['titulo']
            pregunta_object.save()
            for respuesta in pregunta['respuestas']:
                respuesta_object = Respuesta.objects.get(pk=respuesta['id'])
                respuesta_object.titulo = respuesta['titulo']
                respuesta_object.correcto = respuesta['correcto']
                respuesta_object.save()
        serializer = EvaluacionSerializer(evaluacion)
        return Response(serializer.data)


class SolveEvaluacionAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        data = request.data

        evaluacion_object = Evaluacion.objects.get(pk=data['evaluacion'])
        estudiante_object = User.objects.get(pk=data['estudiante'])

        evaluacion_resuelta = EvaluacionResuelta.objects.create(
            evaluacion = evaluacion_object,
            estudiante = estudiante_object,
        )
        aciertos = 0
        for r in data['respuestas']:
            respuesta = Respuesta.objects.get(pk=r)
            if respuesta.correcto:
                aciertos += 1
            RespuestaSeleccionada.objects.create(
                respuesta = respuesta,
                evaluacion_resuelta = evaluacion_resuelta,
            )
        evaluacion_resuelta.ponderacion = aciertos
        evaluacion_resuelta.save()
        serializer = EvaluacionResueltaSerializer(evaluacion_resuelta)
        return Response(serializer.data)


class SolvedEvaluacionesListAPIView(ListAPIView):
    serializer_class = EvaluacionResueltaSerializer
    queryset = EvaluacionResuelta.objects.all()
    permission_classes = (IsAuthenticated, )


class SolvedEvaluacionesRetrieveAPIView(RetrieveAPIView):
    serializer_class = EvaluacionResueltaSerializer
    queryset = EvaluacionResuelta.objects.all()
    permission_classes = (IsAuthenticated, )