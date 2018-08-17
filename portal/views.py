from django.shortcuts import render, render_to_response
from portal.models import Product, Category
from portal.forms import ProductForm

def home(request):
    return render(request, 'portal/home.html',{})

def my_products(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products
    }

    return render(request, 'portal/my_products.html', context)

def product_new(request):
    categories = Category.objects.all()
    form = ProductsForm()

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'portal/product_new.html', context)
