# Generated by Django 4.1.2 on 2022-11-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_cat_offer_is_active_product_offer_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='offer',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product_details',
            name='c_offer',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product_details',
            name='c_offer_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product_details',
            name='p_offer_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='p_offer',
            field=models.FloatField(default=0),
        ),
    ]