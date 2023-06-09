import razorpay
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Carousel, Customer, OrderPlaced, Payment, Product, Wishlist
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cart.models import Cart



def home(request):
    obj = Carousel.objects.all()
    context = {
        'obj' : obj
    }
    prod = Product.objects.all()
    context = {
        'prod' : prod
    }
    wishitem = 0
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'application/index-2.html',locals())



def about(request):
    obj = Carousel.objects.all()
    context = {
        'obj': obj
    }
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'application/about.html', locals())


class CategoryView(View):
    def get(self, request, value):
        wishitem = 0
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=value)
        products = Product.objects.all()
        context = {
            'products': products
        }
        title = Product.objects.filter(category=value).values('title')
        return render(request, 'application/category.html',locals())



class CategoryTitle(View):
    def get(self, request, value):
        wishitem = 0
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(title=value)
        products = Product.objects.all()
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'application/category.html', locals())


class ParentCategoryView(View):
    def get(self, request, value):
        wishitem = 0
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(parent_category=value)
        products = Product.objects.all()
        context = {
            'products': products
        }
        title = Product.objects.filter(parent_category=value).values('title')
        return render(request, 'application/parent_category.html', locals())


class ParentCategoryTitle(View):
    def get(self, request, value):
        wishitem = 0
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(title=value)
        products = Product.objects.all()
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'application/parent_category.html', locals())



class ProductDetail(View):
    def get(self, request,pk):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.get(pk=pk)
        products = Product.objects.all()
        context = {
            'products': products
        }
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        return render(request, 'application/product_detail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        total_item = 0
        wish_item = 0
        if request.user.is_authenticated:
            total_item = len(Cart.objects.filter(user=request.user))
            wish_item = len(Wishlist.objects.filter(user=request.user))
        form = CustomerRegistrationForm()
        return render(request, 'application/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш аккаунт успешно зарегистрирован!')
        else:
            messages.warning(request,"Проверьте введённые данные!")
        return render(request, 'application/customerregistration.html', locals())



class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'application/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            req = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile,
                           state=state, zipcode=zipcode)
            req.save()
            messages.success(request, 'Изменения успешно сохранены!')
        else:
            messages.warning(request,"Проверьте введённые данные!")
        return render(request, 'application/profile.html', locals())



def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'application/address.html', locals())



class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'application/updateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'Изменения успешно сохранены!')
        else:
            messages.warning(request,"Проверьте введённые данные!")
        return redirect('address',locals())


def delete_address(request, pk=None):
    add = get_object_or_404(Customer, pk=pk, user=request.user)
    if request.method  == 'GET':
        add.delete()
        return redirect('profile')
    context = {'add': add}




()
def show_wishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request, 'application/wishlist.html', locals())



class checkout(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 150
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = {'amount': razoramount, "currency": "INR", "receipt": "order_rcptid_12"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        #{'id': 'order_LkRnNLrbYhsZlh', 'entity': 'order', 'amount': 105000, 'amount_paid': 0, 'amount_due': 105000, 'currency': 'INR', 'receipt': 'order_rcptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1682954750}
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user = user,
                amount = totalamount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status
            )
            payment.save()
        return render(request, 'application/checkout.html', locals())



def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    #print("payment_done : oid = ",order_id" pid = ",payment_id," cid = ",cust_id)
    user = request.user
    #return redirect("orders")
    customer = Customer.objects.get(id=cust_id)
    #To update payment status and payment id
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    #To save order details
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()
    return redirect("orders")



def orders(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'application/orders.html', locals())





def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data={
            'message': 'Wishlist Added successfully'
        }
        return JsonResponse(data)



def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data={
            'message': 'Wishlist Removed successfully'
        }
        return JsonResponse(data)


def delete_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data={
            'message': 'Wishlist Removed successfully'
        }
        return JsonResponse(data)



def search(request):
    query = request.GET.get('search')
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(title__icontains=query)
    return render(request, "application/search.html", locals())