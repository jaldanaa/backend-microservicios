from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from .permissions import (
    HasEditEvaluationPermission,
    HasSolveEvaluationPermission,
    HasCreateEvaluationPermission,
)

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

from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied



class CursoViewSet(ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    permission_classes = (IsAuthenticated, )


def solved_evaluation(available_evaluations_list, solved_evaluations_list):
    queryset = []
    for ae in available_evaluations_list:
        already_solved = False
        for se in solved_evaluations_list:
            if ae.id == se.evaluacion.id: already_solved = True
        if not already_solved: queryset.append(ae)
    return queryset


def get_evaluaciones_queryset(user, user_type):
    if user_type == 1:
        queryset = Evaluacion.objects.all()
    if user_type == 2:
        queryset = Evaluacion.objects.filter(catedratico=user)
    if user_type == 3:
        evaluaciones_resueltas = EvaluacionResuelta.objects.filter(estudiante=user)
        evaluaciones_disponibles = Evaluacion.objects.all()
        queryset = solved_evaluation(evaluaciones_disponibles, evaluaciones_resueltas)
    return queryset


class EvaluacionList(ListAPIView):
    serializer_class = EvaluacionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_type = self.request.user.profile.tipo
        user = self.request.user
        return get_evaluaciones_queryset(user, user_type)
        

class EvaluacionRetrieve(RetrieveAPIView):
    serializer_class = EvaluacionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Evaluacion.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def check_object_permissions(self, request, obj):
        user_type = request.user.profile.tipo
        user = request.user
        permission_denied = False
        if user_type == 1:
            return True
        if user_type == 2 and user.id != obj.catedratico.id:
            permission_denied = True
        if user_type == 3:
            queryset = []
            solved_by_student = EvaluacionResuelta.objects.filter(estudiante=user)
            permission_denied = False
            for sbs in solved_by_student:
                if obj.id == sbs.evaluacion.id: permission_denied = True
        if permission_denied:
            raise PermissionDenied()


class CreateEvaluacionAPIView(APIView):
    permission_classes = (IsAuthenticated, HasCreateEvaluationPermission)

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
    permission_classes = (IsAuthenticated, HasEditEvaluationPermission)

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
    permission_classes = (IsAuthenticated, HasSolveEvaluationPermission)

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
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return solved_evaluations(self.request.user.profile.tipo, self.request.user)


class SolvedEvaluacionesRetrieveAPIView(RetrieveAPIView):
    serializer_class = EvaluacionResueltaSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return solved_evaluations(self.request.user.profile.tipo, self.request.user)


def solved_evaluations(user_type, user):
    if user_type == 1:
        return EvaluacionResuelta.objects.all()
    if user_type == 2:
        return EvaluacionResuelta.objects.filter(evaluacion__catedratico=user)
    if user_type == 3:
        return EvaluacionResuelta.objects.filter(estudiante=user)