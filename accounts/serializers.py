from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User

from restaurant.serializers import RestaurantReadSerializer


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    def validate(self, data):
        data['email'] = data['email'].lower()
        username = data.get('email')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError(
                "Invalid Credentials", code='authorization')
        else:
            return data


class UserSerializer(serializers.ModelSerializer):
    restaurant = RestaurantReadSerializer(many = True, read_only = True)
    class Meta:
        model = User
        fields = ['id','email','name','password','city','state','zipcode','restaurant','balance','phone',]
        read_only_fields = ['balance']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        email = email.lower()
        if self.instance is not None and self.instance.email != email:
            raise serializers.ValidationError('email cannot be updated')
        return email

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            name = validated_data['name'],
            city = validated_data['city'],
            state = validated_data['state'],
            zipcode = validated_data['zipcode'],
            phone = validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr,value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
