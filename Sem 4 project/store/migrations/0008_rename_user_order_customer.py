# Generated by Django 3.2 on 2021-06-19 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_pincode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]
