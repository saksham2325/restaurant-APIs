from restaurant import models
from restaurant import serializers as srlzr
from rest_framework import viewsets


class RestaurantViewset(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = srlzr.RestaurantSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = srlzr.OrderSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = models.Food.objects.all()
    serializer_class = srlzr.FoodSerializer


class OrderFoodViewSet(viewsets.ModelViewSet):
    queryset = models.OrderFood.objects.all()
    serializer_class = srlzr.OrderFoodSerializer
