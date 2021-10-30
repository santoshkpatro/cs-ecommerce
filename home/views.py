from django.shortcuts import render, redirect
from products.models import Product
from home.models import Contact


def index(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'home/index.html', context=data)


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'home/detail.html', {'product': product})


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        description = request.POST['description']

        contact = Contact(email=email,
                          phone=phone,
                          subject=subject,
                          description=description
                          )
        contact.save()
        return redirect('index')
    return render(request, 'home/contact.html')
