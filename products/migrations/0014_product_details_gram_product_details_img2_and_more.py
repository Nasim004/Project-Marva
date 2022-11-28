# Generated by Django 4.1.2 on 2022-11-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_coupons_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='gram',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_details',
            name='img2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='assets/images'),
        ),
        migrations.AddField(
            model_name='product_details',
            name='img3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='assets/images'),
        ),
        migrations.AddField(
            model_name='product_details',
            name='img4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='assets/images'),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='assets/images'),
        ),
    ]