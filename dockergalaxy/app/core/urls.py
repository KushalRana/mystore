from django.urls import path
from core.views import *

app_name = "core"

urlpatterns = [
    path('', index, name='index'),
    path('category/', category_list_view, name='category-list'),
    path('category/<title>/', category_subcategory_list_view, name='category-subcategory-list'),
    path('subcategory/<title>/', subcategory_product_list_view, name='subcategory-product-list'),
    path('product/<pid>', product_detail_view, name='product-detail'),
    path('product/', product_view, name='product'),
]
