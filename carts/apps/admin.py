from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register([Products, Category, Cart, CartProduct, Order, Customer])

