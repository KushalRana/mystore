from django.db import models
# from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe
from userauths.models import User
import uuid
# Create your models here.

STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),

)

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("in_review", "In Review"),
    ("rejected", "Rejected"),
    ("published", "Published"),
)

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):

    cid = models.UUIDField(default=uuid.uuid4, max_length=10)
    title = models.CharField(max_length=100, default="MEN")
    image = models.ImageField(upload_to='category', null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Tags(models.Model):
    pass


class Vendor(models.Model):
    vid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=10)

    title = models.CharField(max_length=100, default="Nesify")
    image = models.ImageField(upload_to=user_directory_path,)
    description = models.TextField(null=True, blank=True, default="New vendor")

    address = models.CharField(max_length=100, default="Nepal")
    contact = models.CharField(
        max_length=100, default="+977 (123) (456) (7890)")
    chat_rspn_time = models.CharField(max_length=100, default="1 Day")
    shipping_time = models.CharField(max_length=100, default="1 Week")
    authentic_rating = models.CharField(max_length=100, default="100%")
    days_return = models.CharField(max_length=100, default="No return")
    warranty_period = models.CharField(max_length=100, default="No warranty")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Vendors'

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100, default="new product")
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(
        null=True, blank=True, default="this is product")

    price = models.DecimalField(max_digits=9999999999, decimal_places=2)
    old_price = models.DecimalField(max_digits=9999999999, decimal_places=2)

    specifications = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True,)

    product_status = models.CharField(
        choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = models.UUIDField(default=uuid.uuid4, max_length=10)

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (100 - (self.price / self.old_price) * 100)
        return new_price


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Images'


############################################ Cart, Order, OrderItems and address##########################################
############################################ Cart, Order, OrderItems and address##########################################
############################################ Cart, Order, OrderItems and address##########################################
############################################ Cart, Order, OrderItems and address##########################################


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2)
    paid_track = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True,)
    product_status = models.CharField(
        choices=STATUS_CHOICE, max_length=30, default="processing")

    class Meta:
        verbose_name_plural = 'Cart Order'


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2)
    total = models.DecimalField(max_digits=9999999999, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Cart Order Items'

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))


############################################ product review, wishlist and address ##########################################
############################################ product review, wishlist and address ##########################################
############################################ product review, wishlist and address ##########################################
############################################ product review, wishlist and address ##########################################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product

    def get_rating(self):
        return self.rating


class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return self.product


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Address'
