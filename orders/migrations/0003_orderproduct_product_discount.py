# Generated by Django 4.2.9 on 2024-02-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_coupon_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='product_discount',
            field=models.FloatField(default=0.0),
        ),
    ]