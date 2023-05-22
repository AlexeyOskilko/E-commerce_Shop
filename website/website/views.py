
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
# from .models import Carousel, Cart, Customer, OrderPlaced, Payment, Product, Wishlist
# from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def home(request):
    # obj = Carousel.objects.all()
    # context = {
    #     'obj' : obj
    # }
    wishitem = 0
    totalitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'website/index-2.html', locals())


# @login_required
def about(request):
    # obj = Carousel.objects.all()
    # context = {
    #     'obj': obj
    # }
    totalitem = 0
    wishitem = 0
    # if request.user.is_authenticated:
        # totalitem = len(Cart.objects.filter(user=request.user))
        # wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'website/about.html', locals())


# @login_required
def contact(request):
    # obj = Carousel.objects.all()
    # context = {
    #     'obj': obj
    # }
    wishitem = 0
    totalitem = 0
    # if request.user.is_authenticated:
        # totalitem = len(Cart.objects.filter(user=request.user))
        # wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'website/contact.html', locals())


# @method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, value):
        wishitem = 0
        totalitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        # product = Product.objects.filter(category=value)
        # title = Product.objects.filter(category=value).values('title')
        return render(request, 'website/category.html',locals())


# @method_decorator(login_required, name='dispatch')
class CategoryTitle(View):
    def get(self, request, value):
        wishitem = 0
        totalitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        # product = Product.objects.filter(title=value)
        # title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'website/category.html', locals())


# @method_decorator(login_required, name='dispatch')
class ProductDetail(View):
    def get(self, request,pk):
        totalitem = 0
        wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        # product = Product.objects.get(pk=pk)
        # wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        return render(request, 'website/product_detail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        total_item = 0
        wish_item = 0
        # if request.user.is_authenticated:
        #     total_item = len(Cart.objects.filter(user=request.user))
        #     wish_item = len(Wishlist.objects.filter(user=request.user))
        # form = CustomerRegistrationForm()
        return render(request, 'website/customerregistration.html', locals())

    def post(self, request):
        # form = CustomerRegistrationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, 'Ваш аккаунт успешно зарегистрирован!')
        # else:
        #     messages.warning(request,"Проверьте введённые данные!")
        return render(request, 'website/customerregistration.html', locals())


# @method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        # form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'website/profile.html', locals())

    def post(self, request):
        # form = CustomerProfileForm(request.POST)
        # if form.is_valid():
        #     user = request.user
        #     name = form.cleaned_data['name']
        #     locality = form.cleaned_data['locality']
        #     city = form.cleaned_data['city']
        #     mobile = form.cleaned_data['mobile']
        #     state = form.cleaned_data['state']
        #     zipcode = form.cleaned_data['zipcode']

        #     req = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile,
        #                    state=state, zipcode=zipcode)
        #     req.save()
        #     messages.success(request, 'Изменения успешно сохранены!')
        # else:
        #     messages.warning(request,"Проверьте введённые данные!")
        return render(request, 'website/profile.html', locals())


# @login_required
def address(request):
    # add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'website/address.html', locals())


# @method_decorator(login_required, name='dispatch')
class updateAddress(View):
    def get(self, request, pk):
        # add = Customer.objects.get(pk=pk)
        # form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'website/updateAddress.html', locals())

    def post(self, request, pk):
        # form = CustomerProfileForm(request.POST)
        # if form.is_valid():
        #     add = Customer.objects.get(pk=pk)
        #     add.name = form.cleaned_data['name']
        #     add.locality = form.cleaned_data['locality']
        #     add.city = form.cleaned_data['city']
        #     add.mobile = form.cleaned_data['mobile']
        #     add.state = form.cleaned_data['state']
        #     add.zipcode = form.cleaned_data['zipcode']
        #     add.save()
        #     messages.success(request, 'Изменения успешно сохранены!')
        # else:
        #     messages.warning(request,"Проверьте введённые данные!")
        return redirect('address')


# @login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    # product = Product.objects.get(id=product_id)
    # card, created = Cart.objects.get_or_create(user=user, product=product)
    # if not created:
    #     card.quantity += 1
    #     card.save()
    return redirect('/cart')

# @login_required
def show_cart(request):
    user = request.user
    # cart = Cart.objects.filter(user=user)
    amount = 0
    # for p in cart:
    #     value = p.quantity * p.product.discounted_price
    #     amount= amount + value
    totalamount = amount + 150
    totalitem = 0
    wishitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'website/addtocart.html', locals())

# @login_required()
def show_wishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    # product = Wishlist.objects.filter(user=user)
    return render(request, 'website/wishlist.html', locals())


# @method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        # user = request.user
        # add = Customer.objects.filter(user=user)
        # cart_items = Cart.objects.filter(user=user)
        # famount = 0
        # for p in cart_items:
        #     value = p.quantity * p.product.discounted_price
        #     famount = famount + value
        # totalamount = famount + 150
        # razoramount = int(totalamount * 100)
        # client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        # data = {'amount': razoramount, "currency": "INR", "receipt": "order_rcptid_12"}
        # payment_response = client.order.create(data=data)
        # print(payment_response)
        # #{'id': 'order_LkRnNLrbYhsZlh', 'entity': 'order', 'amount': 105000, 'amount_paid': 0, 'amount_due': 105000, 'currency': 'INR', 'receipt': 'order_rcptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1682954750}
        # order_id = payment_response['id']
        # order_status = payment_response['status']
        # if order_status == 'created':
        #     payment = Payment(
        #         user = user,
        #         amount = totalamount,
        #         razorpay_order_id = order_id,
        #         razorpay_payment_status = order_status
        #     )
        #     payment.save()
        return render(request, 'website/checkout.html', locals())


# @login_required
# def payment_done(request):
#     order_id = request.GET.get('order_id')
#     payment_id = request.GET.get('payment_id')
#     cust_id = request.GET.get('cust_id')
#     #print("payment_done : oid = ",order_id" pid = ",payment_id," cid = ",cust_id)
#     user = request.user
#     #return redirect("orders")
#     customer = Customer.objects.get(id=cust_id)
#     #To update payment status and payment id
#     payment = Payment.objects.get(razorpay_order_id=order_id)
#     payment.paid = True
#     payment.razorpay_payment_id = payment_id
#     payment.save()
#     #To save order details
#     cart = Cart.objects.filter(user=user)
#     for c in cart:
#         OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
#         c.delete()
#     return redirect("orders")


# @login_required
def orders(request):
    totalitem = 0
    wishitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    # order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'website/orders.html', locals())


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


# def plus_wishlist(request):
#     if request.method == 'GET':
#         prod_id = request.GET['prod_id']
#         product = Product.objects.get(id=prod_id)
#         user = request.user
#         Wishlist(user=user, product=product).save()
#         data={
#             'message': 'Wishlist Added successfully'
#         }
#         return JsonResponse(data)



# def minus_wishlist(request):
#     if request.method == 'GET':
#         prod_id = request.GET['prod_id']
#         product = Product.objects.get(id=prod_id)
#         user = request.user
#         Wishlist.objects.filter(user=user, product=product).delete()
#         data={
#             'message': 'Wishlist Removed successfully'
#         }
#         return JsonResponse(data)


# @login_required
# def search(request):
#     query = request.GET['search']
#     totalitem = 0
#     wishitem = 0
#     if request.user.is_authenticated:
#         totalitem = len(Cart.objects.filter(user=request.user))
#         wishitem = len(Wishlist.objects.filter(user=request.user))
#     product = Product.objects.filter(Q(title__icontains=query))
#     return render(request, "website/search.html", locals())