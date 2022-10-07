from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "rating", "offer")


admin.site.register(Product, ProductAdmin)
