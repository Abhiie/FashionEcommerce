from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customers
from django.http import HttpResponse
from tkinter import *
from tkinter import messagebox
from .models.customer import Customers
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models.orders import Order


# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get("pid")
        cart = request.session.get('cart')
        if cart:
            quan = cart.get(product)
            if quan:
                cart[product] = quan + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print("cart ", request.session['cart'])
        return redirect('indexpage')

    def get(self, request):
        products = None
        cat = Category.get_cat()
        catId = request.GET.get('category')
        if catId:
            products = Product.get_products_byId(catId)
        else:
            products = Product.get_products()
        data = {}
        data['products'] = products
        data['cat'] = cat
        print("You are : ", request.session.get('UserEmail_id'))
        return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'Registration.html')
    else:

        f_name = request.POST.get('txtFName')
        l_name = request.POST.get('txtLName')
        contact = request.POST.get('txtCno')
        email = request.POST.get('txtEmail')
        password = request.POST.get('txtPwd')
        print(f_name, l_name, contact, email, password)
        customer = Customers(first_name=f_name, last_name=l_name, phone=contact, email=email, password=password)
        top = Tk()

        top.geometry("100x100")
        isE = customer.ifthere()
        if isE:
            messagebox.showinfo("error", "Email already exist")
            top.mainloop()
            return redirect("indexpage")

        else:
            customer.password = make_password(customer.password)
            customer.register()
            messagebox.showinfo("information", "Successfully Resgistered!")
            top.mainloop()
            return redirect("indexpage")


class Login(View):
    def get(self, request):
        return render(request, 'Login.html')

    def post(self, request):
        email = request.POST.get("Username")  # dictionary
        pwd = request.POST.get("Pwd")  # dictionary
        customer = Customers.getUser(email)
        if customer:
            f = check_password(pwd, customer.password)
            if f:
                request.session['customer'] = customer.id
                #  request.session['UserEmail_id'] = customer.email

                return redirect("indexpage")
            else:
                top = Tk()
                messagebox.showinfo("error", "Email or pwd is not correct")
                top.mainloop()
        else:
            top = Tk()
            messagebox.showinfo("error", "Email or pwd is not correct")
            top.mainloop()

        print(customer)
        print(email, pwd)
        return render(request, 'Login.html')


def logout(request):
    request.session.clear()
    return redirect("indexpage")


class cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_cart(ids)
        print(products)
        return render(request, 'Cart.html', {'products': products})


def AddressPage(request):
    return render(request, 'AddressPage.html')


class Checkout(View):
    def post(self, request):
        address = request.POST.get('txtFName')
        pincode=request.POST.get('txtPincode')
        phone = request.POST.get('txtCno')
        customer = request.session.get('customer')
        cart1 = request.session.get('cart')
        products = Product.get_products_cart(list(cart1.keys()))
        print(address, phone, customer, cart1, products)

        for product in products:
            order = Order(customer=Customers(id=customer),
                             product=product,
                             price=product.price,
                             address=address,
                             phoneNo=phone,
                          pincode=pincode,

                             quantity=cart1.get(str(product.id)))

            order.save()
        request.session['cart'] = {}
        return redirect('Cart')



class OrderHis(View):
    def get(self,request):
        cust = request.session.get('customer')
        orders = Order.get_order_cust(cust)
        print(orders)
        return render(request,"OrdersHistory.html",{'orders': orders})