from django.contrib import admin
from .models import Carousel, Customer, OrderPlaced, Payment, Product, Wishlist
from django.utils.html import format_html
from django.urls import reverse
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'displayed_name', 'taste', 'discounted_price', 'category', 'parent_category', 'product_image',]

@admin.register(Carousel)
class CarouselModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sub_title', 'image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'mobile', 'zipcode', 'state']





@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid' ]


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customers', 'products', 'quantity', 'ordered_date', 'status', 'payments']

    def customers(self,obj):
        link = reverse('admin:application_customer_change',args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def products(self,obj):
        link = reverse('admin:application_product_change',args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def payments(self,obj):
        link = reverse('admin:application_payment_change',args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)


@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products']

    def products(self,obj):
        link = reverse('admin:application_product_change',args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)