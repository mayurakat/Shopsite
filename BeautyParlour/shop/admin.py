from django.contrib import admin
from shop.models import cart, cart_product, product

# Register your models here.
admin.site.register(product)
admin.site.register(cart_product)
admin.site.register(cart)