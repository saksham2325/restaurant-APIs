from rest_framework import serializers

from restaurant import models

class RestaurantReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ['id','name']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ['id','name','state','city','zipcode','owner']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = "__all__"


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderFood
        fields = "__all__"
        