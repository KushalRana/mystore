# Generated by Django 4.2.5 on 2023-09-26 10:31

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_category_cid_alter_product_sku_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=core.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.ImageField(upload_to='product-images'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.CharField(default='Nepal', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='authentic_rating',
            field=models.CharField(default='100%', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='chat_rspn_time',
            field=models.CharField(default='1 Day', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='days_return',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(upload_to=core.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='shipping_time',
            field=models.CharField(default='1 Week', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='warranty_period',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
