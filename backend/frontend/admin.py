from django.contrib import admin
from .models import Product, Comment, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'tags', 'description', 'product_image', 'price')


admin.site.register((Product, Comment, Cart))
