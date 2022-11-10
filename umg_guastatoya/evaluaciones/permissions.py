from rest_framework.permissions import BasePermission
from .models import (
    Evaluacion,
    EvaluacionResuelta
)

class HasEditEvaluationPermission(BasePermission):
    """
    Verifies if the logged in user is admin then it will allow to edit any 
    """
    def has_permission(self, request, view):
        user_type = request.user.profile.tipo
        user = request.user
        if user_type == 1: return True

        if user_type == 2:
            evaluacion = Evaluacion.objects.get(pk=request.data['id'])
            return evaluacion.catedratico.id == user.id
        return False


class HasSolveEvaluationPermission(BasePermission):
    """
        Verifies if the logged in user making the request is a student and the evaluation to solve has not been solved before
    """
    def has_permission(self, request, view):
        user_type = request.user.profile.tipo
        user = request.user
        
        if (user_type != 3): return False

        evaluacion_object = Evaluacion.objects.get(pk=request.data['evaluacion'])

        evaluaciones_resueltas = EvaluacionResuelta.objects.filter(estudiante=user)
        return self.available_evaluation(evaluacion_object, evaluaciones_resueltas)

    def available_evaluation(self, available_evaluation, solved_evaluations_list):
        for se in solved_evaluations_list:
            if se.evaluacion.id == available_evaluation.id: return False
        return True


class HasCreateEvaluationPermission(BasePermission):
    """
        Verifies if the logged in user making the request is admin or teacher
    """
    def has_permission(self, request, view):
        return request.user.profile.tipo == 1 or request.user.profile.tipo == 2