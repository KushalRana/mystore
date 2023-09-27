from django.contrib import admin
from core.models import *

# Register your models here.


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['product_image', 'title', 'category',
                    'price', 'featured', 'product_status', 'user',]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_image', 'title', 'cid']


class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_image', 'title',
                    'contact', 'address', 'description',]


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'order_date', 'product_status']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item',
                    'image', 'quantity', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'review', 'rating']


class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist, wishlistAdmin)
admin.site.register(Address, AddressAdmin)
