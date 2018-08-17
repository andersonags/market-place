from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'my_products', views.my_products, name='my_products'),
    path(r'product/new', views.product_new, name='product_new'),
]
