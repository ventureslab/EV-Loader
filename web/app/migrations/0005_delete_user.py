# Generated by Django 3.1 on 2020-12-12 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_fiat_currency'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
