from django.contrib import admin
from .models import Stocks, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Stocks)