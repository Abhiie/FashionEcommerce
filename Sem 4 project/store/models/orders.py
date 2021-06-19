from django.db import models
from .product import Product
from .customer import Customers
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    address = models.CharField(max_length=200,default='',blank=True)
    phoneNo = models.CharField(max_length=14,default='',blank=True)
    pincode = models.CharField(max_length=10,default='',blank=True)
    status = models.BooleanField(default=False)

    def placeorder(self):
        self.save()

    @staticmethod
    def get_order_cust(customer_id):
        return Order.objects.filter(customer = customer_id)