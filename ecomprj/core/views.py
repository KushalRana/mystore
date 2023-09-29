from django.shortcuts import render
from core.models import Product, Category

# Create your views here.


def index(request):
    product = Product.objects.filter(
        product_status="published", featured=True).order_by("-date")

    context = {
        'products': product,
    }

    return render(request, 'core/index.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }

    return render(request, 'core/category-list.html', context)