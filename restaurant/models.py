from django.db import models

from accounts import models as account_models
from common.models import CreatedUpdatedAt


class Restaurant(CreatedUpdatedAt):
    owner = models.ForeignKey(account_models.User,on_delete = models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)
    

class Order(CreatedUpdatedAt):
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    status = models.IntegerField()
    user = models.ForeignKey(account_models.User,on_delete = models.CASCADE)
    total_price = models.DecimalField(max_digits = 10,decimal_places = 2)


class Food(CreatedUpdatedAt):
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    quantity_available = models.IntegerField()


class OrderFood(CreatedUpdatedAt):
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    food = models.ForeignKey(Food,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
