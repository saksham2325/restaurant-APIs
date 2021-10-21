from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.manager import UserManager
from common.models import CreateAndUpdateTime


class User(AbstractUser,CreateAndUpdateTime):
    """
    This is the User Model.

    This User Model is made by inheriting the AbstractUser and CreateAndUpdateTime class
    It has several attributes like email, name, address, phone number and balance of the
    User.
    """
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=19,decimal_places=2,default=1000)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
