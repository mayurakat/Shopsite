from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shop,name='shop'),
    path('addtocart',views.addcart,name='addtocart'),
    path('placed',views.placed,name='placed'),
   
]