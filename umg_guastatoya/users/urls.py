  
from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('profiles', views.ProfileViewSet, basename='profiles')

urlpatterns = [
  path('', include(router.urls)),
  path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('create-student/', views.CreateStudentCreateAPIView.as_view(), name='create-student'),
  path('update-student-profile/<int:pk>/', views.StudentProfileUpdateAPIView.as_view(), name='update-student-profile'),
]