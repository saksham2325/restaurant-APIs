from django.db import models

from accounts import models as account_models
from common import constants
from common.models import CreateAndUpdateTime


class Restaurant(CreateAndUpdateTime):
    """
    This is the Restaurant model.

    It inherits the CreatAndUpdateTime class and it has several fields like owner, name and
    address of the restaurant.
    """
    owner = models.ForeignKey(account_models.User,on_delete=models.CASCADE,null=True,related_name="restaurant")
    name = models.CharField(max_length=constants.NAME)
    city = models.CharField(max_length=constants.ADDRESS)
    state = models.CharField(max_length=constants.ADDRESS)
    zipcode = models.CharField(max_length=constants.ZIPCODE)

    def __str__(self):
        return self.name
    

class Order(CreateAndUpdateTime):
    """
    This is the Order Model.

    It inherits the CreatAndUpdateTime class and it has several fields like restaurant to
    which the order is associated with, current status of the order, user to which order 
    is associated with and the total price of the Order.
    """
    STATUS_CHOICES = (
        (constants.ACCEPTED,'Rejected'),
        (constants.ACCEPTED,'Accepted'),
        (constants.DISPATCHED,'Dispatched'),
        (constants.DELIVERED,'Delivered'),
        (constants.CANCELLED,'Cancelled'),
        (constants.PLACED,'Placed'),
    )
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES,default=constants.PLACED)
    user = models.ForeignKey(account_models.User,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=constants.MAXPRICE,decimal_places=constants.DECIMALPLACE)

    def __str__(self):
        return self.restaurant


class Food(CreateAndUpdateTime):
    """
    This is the Food Model.

    It inherits the CreatAndUpdateTime class and it has several fields like restaurant to
    which the food is associated with, price of the Food and the quantity available for 
    that food.
    """
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=constants.PRICE,decimal_places=constants.DECIMALPLACE)
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.restaurant


class OrderFood(CreateAndUpdateTime):
    """
    This is the OrderFood Model.

    It inherits the CreatAndUpdateTime class and it describes the relation between Order
    and Food. It has several fields like order, food, quantity and the price.
    """
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=constants.PRICE,decimal_places=constants.DECIMALPLACE)

    def __str__(self):
        return self.order
