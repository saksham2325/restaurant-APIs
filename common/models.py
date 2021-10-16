from django.db import models

class CreatedUpdatedAt(models.Model):
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True
