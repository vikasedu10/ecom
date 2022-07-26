from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # path('products', views.products, name='products'),
    path('product/<int:id>/view', views.product, name='product'),
    path('contact', views.contact, name='contact'),
    path('products/<str:category>/view', views.product_by_category, name='product_by_category'),
    path('add/product', views.add_product, name='add_product'),
    path('add/<int:id>/cart', views.add_to_cart, name='add_to_cart'),
    path('cart/checkout', views.cart_checkout, name='cart_checkout'),
    path('cart/checkout/payment/view', views.payment_success, name='payment_success'),
]  
