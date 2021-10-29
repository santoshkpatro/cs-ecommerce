from django.shortcuts import render
from products.models import Product


def index(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'home/index.html', context=data)


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'home/detail.html', {'product': product})
