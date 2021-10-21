from rest_framework import serializers

from restaurant.models import (Food, Order, OrderFood, Restaurant)

class RestaurantReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','state','city','zipcode','owner']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = "__all__"
        