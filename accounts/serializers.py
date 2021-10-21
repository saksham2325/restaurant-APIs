from rest_framework import serializers
from accounts.models import User

from restaurant.serializers import RestaurantReadSerializer


class UserSerializer(serializers.ModelSerializer):
    restaurant = RestaurantReadSerializer(many = True, read_only = True)

    class Meta:
        model = User
        fields = ['id','email','name','password','city','state','zipcode','restaurant','balance','phone']
        read_only_fields = ['balance']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            city=validated_data['city'],
            state=validated_data['state'],
            zipcode=validated_data['zipcode'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
