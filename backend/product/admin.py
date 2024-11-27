from django.contrib import admin
from .models import Product, ProductBatch, Transaction

admin.site.register(Product)
admin.site.register(ProductBatch)
admin.site.register(Transaction)
