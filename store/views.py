from django.shortcuts import render,get_object_or_404
from .models import Category, Product, ProductImage
from cart.forms import CartAddProductForm

def all_products(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'store/all_products.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    image_list = product.images.all()
    cart_product_form = CartAddProductForm()
    
    context = {
        'images': image_list,
        'product':product,
        'cart_product_form':cart_product_form,
    }

    return render(request, 'store/detail_product.html', context)

def category_detail(request, category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category, available=True)
    
    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'store/category_detail.html', context)
