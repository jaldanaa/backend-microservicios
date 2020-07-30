  
from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
  path('', include(router.urls)),
  path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]