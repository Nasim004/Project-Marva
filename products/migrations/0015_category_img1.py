# Generated by Django 4.1.2 on 2022-11-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_details_gram_product_details_img2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='assets/images'),
        ),
    ]