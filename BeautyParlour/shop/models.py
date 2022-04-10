from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from venv import create
from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="p_images")


class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(default=datetime.now)




class cart_product(models.Model):
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField('Total',default=0)