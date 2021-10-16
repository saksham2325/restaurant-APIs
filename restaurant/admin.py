from django.contrib import admin

from restaurant.models import (Food, Order, OrderFood, Restaurant)

admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(OrderFood)
