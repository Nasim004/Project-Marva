# Generated by Django 4.1.2 on 2022-10-27 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_details_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_details',
            name='dis_price',
        ),
    ]