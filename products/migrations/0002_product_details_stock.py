# Generated by Django 4.1.2 on 2022-10-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
