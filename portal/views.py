from django.shortcuts import render, render_to_response
from portal.models import Product

def home(request):
    return render(request, 'portal/home.html',{})

def my_products(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products
    }

    return render(request, 'portal/my_products.html', context)
