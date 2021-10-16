from rest_framework import viewsets

from restaurant.models import (Food, Order, OrderFood, Restaurant)
from restaurant.serializers import (FoodSerializer, OrderFoodSerializer, OrderSerializer, RestaurantSerializer)

class RestaurantViewset(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class OrderFoodViewSet(viewsets.ModelViewSet):
    queryset = OrderFood.objects.all()
    serializer_class = OrderFoodSerializer
