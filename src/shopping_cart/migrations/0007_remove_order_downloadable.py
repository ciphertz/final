# Generated by Django 2.2 on 2019-06-13 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0006_order_downloadable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='downloadable',
        ),
    ]
