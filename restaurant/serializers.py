from rest_framework import serializers

from restaurant import models as restaurant_models

class RestaurantReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant_models.Restaurant
        fields = ['id','name']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant_models.Restaurant
        fields = ['id','name','state','city','zipcode','owner']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant_models.Order
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant_models.Food
        fields = "__all__"


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant_models.OrderFood
        fields = "__all__"
