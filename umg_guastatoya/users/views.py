from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView, UpdateAPIView

from users.serializers import (
    UserSerializer,
    ProfileSerializer,
    UserProfileSerializer,
)

from users.models import (
    Profile
)

from django.contrib.auth.models import User

from django.forms.models import model_to_dict

from .permissions import IsAdmin


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_serializer = UserProfileSerializer(user)
        token['user'] = user_serializer.data
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateStudentCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class StudentProfileUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def partial_update(self, request, *args, **kwargs):
        response = super(StudentProfileUpdateAPIView, self).partial_update(request, *args, **kwargs)
        perfil_updated = Profile.objects.get(pk=request.data['id'])
        perfil_updated.tipo = 3
        perfil_updated.save()
        perfil_updated.user.set_password(perfil_updated.raw_password)
        perfil_updated.user.save()
        return response


class UserViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UserProfileSerializer
        return UserSerializer


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)

    def partial_update(self, request, *args, **kwargs):
        response = super(ProfileViewSet, self).partial_update(request, *args, **kwargs)
        perfil_updated = Profile.objects.get(pk=request.data['id'])
        perfil_updated.save()
        perfil_updated.user.set_password(perfil_updated.raw_password)
        perfil_updated.user.save()
        return response
