# Generated by Django 4.1.2 on 2022-10-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='landmark',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
