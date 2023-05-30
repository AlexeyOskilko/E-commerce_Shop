from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Cart

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

    def products(self,obj):
        link = reverse('admin:application_product_change',args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)