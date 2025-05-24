from django.contrib import admin
from store.models import Product, CartItem, Order, OrderItem
# Register your models here.

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)