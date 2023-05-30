from django.db import models
from django.contrib.auth.models import User
from application.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_cost(self, quantity):
        return quantity * self.product.discounted_price