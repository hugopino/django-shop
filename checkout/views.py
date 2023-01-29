from django.shortcuts import render, redirect
from .checkout import Checkout
from shop.models import Product


def add_product(request, product_id):
    checkout = Checkout(request)
    product = Product.objects.get(id=product_id)
    checkout.add_to_cart(product=product)
    return redirect('shop')

def delete_product(request, product_id):
    checkout = Checkout(request)
    product = Product.objects.get(id=product_id)
    checkout.delete_product(product=product)
    return redirect('shop')

def decrement_product(request, product_id):
    checkout = Checkout(request)
    product = Product.objects.get(id=product_id)
    checkout.decrement_product(product=product)
    return redirect('shop')

def clear_cart(request):
    checkout = Checkout(request)
    checkout.clear_cart()
    return redirect('shop')