from tabnanny import verbose
from django.db import models
from main.views import *

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    last_name = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    message = models.TextField(verbose_name='Message')
    sent_at = models.DateField(auto_now_add=True, verbose_name='Date')


class Order(models.Model):
    product = models.CharField(max_length=500, verbose_name='Order')
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, verbose_name='Client')
    total_price = models.IntegerField(verbose_name='Total price')
    phone = models.IntegerField(verbose_name='Phone number')
    address = models.CharField(max_length=500, null=True, verbose_name='Addres')
    date = models.DateField(auto_now_add=True, verbose_name='Date')


