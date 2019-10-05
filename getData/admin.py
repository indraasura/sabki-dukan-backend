from django.contrib import admin
from .models import Product, PhoneUser, Transactions

# Register your models here.
admin.site.register(Product)
admin.site.register(PhoneUser)
admin.site.register(Transactions)