# Generated by Django 4.1.2 on 2022-11-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_category_offer_product_details_c_offer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_offer',
            name='up_to',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
