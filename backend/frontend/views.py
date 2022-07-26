from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from frontend.models import Product, Comment, Cart

@login_required
def home(request):
    if request.method == 'POST':
        if  request.POST['by_price']:
            print("*&*&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print("*&*&&&&&&&&&&&&&&&&&&&&&&&&&&")
            products = Product.objects.all().order_by('-price')
        # else:
        #     print("*&*&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     products = Product.objects.all().order_by('-name')
    else:
        products = Product.objects.all()
    cart_products = Cart.objects.filter(user=request.user)
    categories = Product.objects.values_list('category', flat=True).distinct()
    params = {
        'products': products,
        'categories': categories,
        'cart_products': cart_products
    }

    return render(request, 'shop/home.html', params)

def product(request, id):
    product = Product.objects.get(id=id) 
    categories = Product.objects.values_list('category', flat=True).distinct()
    cart_products = Cart.objects.filter(user=request.user)
    params = {
        'product': product,
        'categories': categories,
        'cart_products': cart_products

    }
    return render(request, 'shop/product.html', params)

def product_by_category(request, category):
    products = Product.objects.filter(category=category)
    categories = Product.objects.values_list('category', flat=True).distinct()
    cart_products = Cart.objects.filter(user=request.user)
    params = {
        'products': products,
        'categories': categories,
        'cart_products': cart_products


    }
    return render(request, 'shop/product_by_category.html', params)

def contact(request):
    cart_checkout = Cart.objects.filter(user=request.user)
    params = {
        'cart_products': cart_checkout,
    }
    return render(request, 'contact.html', params)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, "Product has been successfully added.")
            return redirect('home')
    else:
        form = ProductForm()
        return render(request, 'shop/home.html', {'form' : form})

def add_to_cart(request, id):
    product_object = Product.objects.get(id=id)
    add_to_cart = Cart(user=request.user, product=product_object)
    add_to_cart.save()
    return redirect("/shop/product/{}/view".format(id))
    
def cart_checkout(request):
    cart_checkout = Cart.objects.filter(user=request.user)
    total_checkout_cost = 0
    for product in cart_checkout:
        total_checkout_cost += product.product.price 
    params = {
        'cart_products': cart_checkout,
        'total_checkout_cost': total_checkout_cost,

    }
    return render(request, 'shop/cart_checkout.html', params)

def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Articles.objects.get(id=postSno)
        product_comment = Comment(comment=comment, user=user, post=post)
        product_comment.save()
        messages.success(
            request, "Comment has been successfully posted in the comment section below.")
    return redirect("article/{}/view".format(postSno))

def payment_success(request):
    cart_products = Cart.objects.all()
    cart_products.delete()
    cart_checkout = Cart.objects.filter(user=request.user)
    params = {
        'cart_products': cart_checkout,
    }
    return render(request, 'shop/payment_success.html', params)
