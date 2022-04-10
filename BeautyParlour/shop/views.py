from pyexpat import model
from re import template
from urllib import request
from venv import create
from django.shortcuts import redirect, render
from .models import product,cart,cart_product
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
# Create your views here.
def shop(request):
    products = product.objects.all()
    return render(request,"shop.html",{'product':products})


def addcart(request):
    if request.method == 'POST':


        product_id = request.POST.get("p_id")
        qty = request.POST.get("qty")
        pd = get_object_or_404(product,pk=product_id)
        carts,created = cart.objects.get_or_create(user=request.user)
        cart_p,_ = cart_product.objects.get_or_create(cart=carts,products=pd)
        cart_p.quantity += int(qty)
        cart_p.total_price = pd.price * cart_p.quantity
        cart_p.save()
        cart_p = cart_product.objects.all()
        cart_total = sum(p.total_price for p in cart_p)
        return render(request,"cart.html",{'cart_p':cart_p,'cart_total':cart_total})

def placed(request):
    return render(request,"placed.html")


