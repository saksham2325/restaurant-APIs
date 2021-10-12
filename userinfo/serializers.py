from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Order
#         fields="__all__"

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Food
#         fields="__all__"

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Order_Food
#         fields="__all__"