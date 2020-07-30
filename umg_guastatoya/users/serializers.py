from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = [
            "id",
            "profile",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
        ]