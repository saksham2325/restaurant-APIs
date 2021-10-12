from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
# router.register(r'order',views.OrderViewSet)
# router.register(r'food',views.FoodViewSet)
# router.register(r'order_food',views.Order_FoodViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
