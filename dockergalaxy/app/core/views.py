from django.shortcuts import render
from core.models import *
from django.db.models import Count

# Create your views here.


def index(request):
    product = Product.objects.filter(
        product_status="published", featured=True).order_by("-date")

    context = {
        'products': product,
    }

    return render(request, 'core/index.html', context)


def category_list_view(request):
    categories = Category.objects.all().annotate(product_count=Count('product'))
    context = {
        "categories": categories,
    }

    return render(request, 'core/category-list.html', context)
    

def category_subcategory_list_view(request,title):
    category = Category.objects.get(title=title)
    subcategories = Subcategory.objects.filter(category=category)

    context = {
        "category": category,
        "subcategories": subcategories,
    }

    return render(request, 'core/category-subcategory-list.html', context)

    
def subcategory_product_list_view(request,title):
    subcategory = Subcategory.objects.get(title=title)
    products = Product.objects.filter(product_status='published', subcategory=subcategory)

    context = {
        "subcategory": subcategory,
        "products": products
    }

    return render(request, 'core/subcategory-product-list.html', context)


def product_view(request):
    product = Product.objects.filter(
        product_status="published").order_by("-date")

    context = {
        'products': product,
    }

    return render(request, 'core/product.html', context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    product_images = ProductImages.objects.all()

    context = {
        'product': product,
        'product_images': product_images,
    }

    return render(request, 'core/product-detail.html', context)