from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    category = [
        ('Fashion', 'Fashion'),
        ('Mobiles and Tablets', 'Mobiles and Tablets'),
        ('Consumer Electronics', 'Consumer Electronics'),
        ('Books', 'Books'),
        ('movie_tickets', 'Movie Tickets'),
        ('baby_products', 'Baby Products'),
        ('Groceries', 'Groceries'),
    ]
    name = models.CharField(default='', blank=True, null=True, max_length=200)
    category = models.CharField(max_length=95, choices=category, blank=True)
    tags = models.CharField(default='', blank=True, null=True, max_length=300)
    description = models.TextField(default='', blank=True, null=True, max_length=900)
    product_image = models.ImageField(upload_to='static/post-images', blank=True, null=True)
    price = models.IntegerField(default=500)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    product_comment = models.CharField(max_length=400, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username.upper() + " commented '" + self.comment[:30] + "...."

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
