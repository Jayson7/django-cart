from django.db import models
from django.contrib.auth.models import User
# Create your models here.

cartes =(
    ("Shoes", "Shoes"),
    ("Clothes", "Clothes"),
)



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Category(models.Model):
    category =  models.CharField(choices=cartes, max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Category"
        


class Products(models.Model):
    name = models.CharField(max_length=300, null=True)
    main_price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField()
    poster = models.ImageField(upload_to="images")
    slug = models.SlugField(unique=True)
    description = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"



class Cart(models.Model):

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart " + str(self.total)

    
    class Meta:
        verbose_name_plural = "Cart"

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    

    def __str__(self):
        return "Cart " + str(self.quantity)

    class Meta:
        verbose_name_plural = "CartProduct"


METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Paypal", "Paypal"),
    ("Quickteller", "Quickteller"),
)

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)
  

    def __str__(self):
        return "Order: " + str(self.id)

    
    class Meta:
        verbose_name_plural = "Order"
