import razorpay
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from application.models import Carousel, Customer, OrderPlaced, Payment, Product, Wishlist
from application.forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .models import Cart


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    card, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        card.quantity += 1
        card.save()
    return redirect('/cart')


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user) #ЗДЕСЬ ВЕРНУТЬ НА ФИЛЬТР ЮЗЕР
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount= amount + value
    totalamount = amount + 150
    totalitem = 0
    wishitem = 0
    # totalitem = len(Cart.objects.filter(user=request.user))
    # wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'cart/addtocart.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 150
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 150
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 150
        data = {
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
