# Generated by Django 4.1.2 on 2022-10-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_address_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(default=8606850230, max_length=15),
            preserve_default=False,
        ),
    ]
