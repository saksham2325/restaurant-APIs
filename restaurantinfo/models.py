from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, update_last_login

class Restaurant(AbstractUser):
    id=models.AutoField(unique=True,primary_key=True)
    owner_id=models.ForeignKey()
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    zipcode=models.CharField(max_length=255)
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()

    


