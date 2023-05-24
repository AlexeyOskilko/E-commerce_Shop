from django.db import models
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('RU', 'Россия'),
    ('UA', 'Украина'),
    ('US', 'США'),
    ('FR', 'Франция'),
)

CATEGORY_CHOICES = (
    ('TE', 'Чай'),
    ('CF', 'Кофе'),
    ('SP', 'Сиропы'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    displayed_name = models.CharField(max_length=50, default="")
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    taste = models.TextField(max_length=200, default="")
    product_image = models.ImageField(upload_to="products", blank=True)
    def __str__(self):
        return self.title


class Carousel(models.Model):
    image = models.ImageField(upload_to="carousel", blank=True)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_cost(self, quantity):
        return quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Принято в работу', 'Принято в работу'),
    ('Сбор заказа', 'Сбор заказа'),
    ('В пути', 'В пути'),
    ('Доставлен', 'Доставлен'),
    ('Отменен', 'Отменен'),
    ('Ожидает', 'Ожидает'),
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Ожидает')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)