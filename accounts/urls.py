from django.contrib import admin
from django.urls import include, path
from django.db import router

from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
# router.register(r'orders',views.OrderViewSet)
# router.register(r'foods',views.FoodViewSet)
# router.register(r'orderfoods',views.OrderFoodViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
