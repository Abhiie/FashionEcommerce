from django.db import models


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=500)#this are used when there is Form api of django

    def register(self):
        self.save()

    def ifthere(self):
        if Customers.objects.filter(email = self.email):
            return True

        return False

    def getUser(email):
        try:
            return Customers.objects.get(email=email)
        except:
            return False
