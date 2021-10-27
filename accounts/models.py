from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from accounts.manager import UserManager
from common import constants
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
    name = models.CharField(max_length=constants.NAME)
    city = models.CharField(max_length=constants.ADDRESS)
    state = models.CharField(max_length=constants.ADDRESS)
    zipcode = models.CharField(max_length=constants.ZIPCODE)
    phone = models.CharField(max_length=constants.PHONE)
    balance = models.DecimalField(max_digits=constants.MAXBALANCE,decimal_places=constants.DECIMALPLACE,default=constants.DEFAULTBALANCE)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
