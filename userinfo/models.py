from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username=None
    id=models.AutoField(unique=True,primary_key=True)
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    zipcode=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    balance=models.FloatField(default=0)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

# class Order(AbstractUser):
#     id=models.AutoField(unique=True,primary_key=True)
#     # restaurant_id=models.ForeignKey()
#     status=models.IntegerField()
#     # user_id=models.ForeignKey()
#     total_price=models.FloatField()
#     created_at=models.DateTimeField()
#     updated_at=models.DateTimeField()
#     USERNAME_FIELD='id'
#     REQUIRED_FIELDS=[]

# class Food(AbstractUser):
#     id=models.AutoField(unique=True,primary_key=True)
#     restaurant_id=models.ForeignKey()
#     price=models.FloatField()
#     quantity_available=models.IntegerField()
#     created_at=models.DateTimeField()
#     updated_at=models.DateTimeField()
    # USERNAME_FIELD='id'
    # REQUIRED_FIELDS=[]

# class Order_Food(AbstractUser):
#     id=models.AutoField(unique=True,primary_key=True)
#     order_id=models.ForeignKey()
#     food_id=models.ForeignKey()
#     quantity=models.IntegerField()
#     price=models.FloatField()
#     created_at=models.DateTimeField()
#     updated_at=models.DateTimeField()
    # USERNAME_FIELD='id'
    # REQUIRED_FIELDS=[]
