from django.db.models import fields
from rest_framework import serializers
from .models import *
# from accounts import serializers as sz

class RestaurantSerializer(serializers.ModelSerializer):
    # owner=sz.UserSerializer()
    class Meta:
        model=Restaurant
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    # restaurantname=RestaurantSerializer()
    class Meta:
        model=Order
        fields="__all__"


class FoodSerializer(serializers.ModelSerializer):
    # restaurantname=RestaurantSerializer()
    class Meta:
        model=Food
        fields="__all__"


class OrderFoodSerializer(serializers.ModelSerializer):
    # order=OrderSerializer()
    # food=FoodSerializer()
    class Meta:
        model=OrderFood
        fields="__all__"
        