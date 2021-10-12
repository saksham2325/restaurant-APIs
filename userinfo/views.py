from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset=Order.objects.all.order_by('name')
#     serializer_class=OrderSerializer


# class FoodViewSet(viewsets.ModelViewSet):
#     queryset=Food.objects.all.order_by('name')
#     serializer_class=FoodSerializer


# class Order_FoodViewSet(viewsets.ModelViewSet):
#     queryset=Order_Food.objects.all.order_by('name')
#     serializer_class=Order_FoodSerializer

# Create your views here.
