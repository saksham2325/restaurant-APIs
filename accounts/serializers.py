from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import User
from restaurant.serializers import RestaurantSerializer

class UserSerializer(serializers.ModelSerializer):

    # user_restaurant = serializers.SerializerMethodField('_get_restaurant_owner')
    # def _get_restaurant_owner(self,user_object):
    #   Restaurant.objects.filter(Restaurant.owner=request.user)
    restaurant = RestaurantSerializer(many = True, read_only = True)
    
    class Meta:
        model = User
        fields = ['email','name','password','city','state','zipcode','balance','restaurant',]
    
    validate_password = make_password
