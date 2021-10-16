from django.urls import include, path
from django.db import router

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
