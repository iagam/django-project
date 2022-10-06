from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def index(request):

    product1 = Product()
    product1.name = "Shoes"
    product1.desc = "Suitable for any terrain"
    product1.price = 40
    product1.rating = 4.98
    product1.img = "product_01.jpg"
    product1.offer = False

    product2 = Product()
    product2.name = "Jackets"
    product2.desc = "All weather jackets"
    product2.price = 75
    product2.rating = 4.8
    product2.img = "product_02.jpg"
    product2.offer = True

    product3 = Product()
    product3.name = "Scarves"
    product3.desc = "Stay warm and cozy"
    product3.price = 10
    product3.rating = 4.9
    product3.img = "product_03.jpg"
    product3.offer = False

    products = [product1, product2, product3]

    return render(request, "index.html", {"products": products})
