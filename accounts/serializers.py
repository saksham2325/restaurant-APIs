from rest_framework import serializers
from accounts.models import User

from restaurant.serializers import RestaurantReadSerializer


class UserSerializer(serializers.ModelSerializer):
    restaurant = RestaurantReadSerializer(many = True, read_only = True)
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','password','city','state','zipcode','restaurant','balance']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
