from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='',null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_cart(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_products():
        return Product.objects.all()

    @staticmethod
    def get_products_byId(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_products()
