from django.contrib import admin

from restaurant import models

admin.site.register(models.Restaurant)
admin.site.register(models.Order)
admin.site.register(models.Food)
admin.site.register(models.OrderFood)
