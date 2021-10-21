from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import CreatedUpdatedAt
from accounts.manager import UserManager


class User(AbstractUser,CreatedUpdatedAt):
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
