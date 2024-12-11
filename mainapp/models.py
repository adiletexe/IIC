from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField()
    bought_price = models.FloatField(max_length=20, null=True)
    sold_price = models.FloatField(max_length=20, blank=True, null=True)
    profit = models.FloatField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=200)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=200, blank=True)
    stocks = models.ManyToManyField(Stocks, blank=True)
    participants = models.CharField(max_length=200, blank=True)
    is_group = models.BooleanField(default=False)
    balance = models.FloatField(max_length=20, default=1000000)
