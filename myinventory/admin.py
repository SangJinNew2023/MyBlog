from django.contrib import admin
from .models import Product, Order


admin.site.site_header="MyInventory Dashboard" #change the admin page title

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)