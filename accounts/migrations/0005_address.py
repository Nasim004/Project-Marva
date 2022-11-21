# Generated by Django 4.1.2 on 2022-10-22 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_details_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('postcode', models.IntegerField()),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('landmark', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user_details')),
            ],
        ),
    ]
