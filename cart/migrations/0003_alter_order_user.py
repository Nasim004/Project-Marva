# Generated by Django 4.1.2 on 2022-11-01 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_address_phone'),
        ('cart', '0002_order_oldcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user_details'),
        ),
    ]
