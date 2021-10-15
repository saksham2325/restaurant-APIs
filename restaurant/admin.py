from django.contrib import admin

from .models import *

admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(OrderFood)
