# Generated by Django 4.1.2 on 2022-11-13 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_coupons_code'),
        ('cart', '0006_oldcart_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='guestCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('user_ref', models.CharField(blank=True, max_length=200, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_details')),
            ],
        ),
    ]