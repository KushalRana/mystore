# Generated by Django 4.2.5 on 2023-09-26 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_order_dates_cartorder_order_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]
