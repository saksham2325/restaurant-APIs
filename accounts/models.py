from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    zipcode=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    balance=models.DecimalField(max_digits=19,decimal_places=2,default=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
