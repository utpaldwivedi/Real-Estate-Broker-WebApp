from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Property(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    image = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=100, blank=True)
    #Latest Traded Price
    ltp = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=10, default="9876543210",unique=True)
    funds = models.PositiveIntegerField(default=0)
    money_invested = models.PositiveIntegerField(default=0)
    pnl = models.IntegerField(default=0)
    portfolio = models.JSONField(null=True, blank=True, default=list)
    watchlist = models.JSONField(null=True, blank=True, default=list)
    pan = models.CharField(max_length=10, default="ABCDE1234F",unique=True)


    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name or self.username
    


class Order(models.Model):
    ORDER_TYPES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)

    def __str__(self):
        return f'{self.order_type} Order for {self.prop.name} at {self.price}'
    
    
class Support(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
