from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    balance = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return "{}".format(self.username)

    def minus_balance(self, to_pay):
        self.balance -= to_pay
        return self.save()

    def plus_balance(self, refund):
        self.balance += refund
        return self.save()


class Product(models.Model):

    objects = None
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def decrease_prod(self, quantity):
        self.stock -= quantity
        return self.save()

    def increase_prod(self, quantity):
        self.stock += quantity
        return self.save()


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=object)
    count = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


