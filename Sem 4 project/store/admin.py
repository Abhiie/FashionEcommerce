from django.contrib import admin
from .models.product import Product
from .models.category import Category

from .models.customer import Customers

from .models.orders import Order
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description', 'image']#used to display table view


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']#used to display table view


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customers)
admin.site.register(Order)
