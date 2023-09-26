from django.shortcuts import render
from core.models import *

# Create your views here.

def index(request):
    product = Product.objects.all()
    
    context = {
        'products':product,
    }
    
    return render(request, 'core/index.html', context)