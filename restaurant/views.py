from restaurant import models as restaurant_models
from restaurant import serializers as restaurant_serializer
from rest_framework import viewsets


class RestaurantViewset(viewsets.ModelViewSet):
    queryset = restaurant_models.Restaurant.objects.all()
    serializer_class = restaurant_serializer.RestaurantSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = restaurant_models.Order.objects.all()
    serializer_class = restaurant_serializer.OrderSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = restaurant_models.Food.objects.all()
    serializer_class = restaurant_serializer.FoodSerializer


class OrderFoodViewSet(viewsets.ModelViewSet):
    queryset = restaurant_models.OrderFood.objects.all()
    serializer_class = restaurant_serializer.OrderFoodSerializer
