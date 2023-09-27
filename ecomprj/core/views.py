from django.shortcuts import render
from core.models import *

# Create your views here.


def index(request):
    product = Product.objects.filter(
        product_status="published", featured=True).order_by("-date")

    context = {
        'products': product,
    }

    return render(request, 'core/index.html', context)
