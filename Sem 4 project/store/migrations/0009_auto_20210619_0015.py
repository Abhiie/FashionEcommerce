# Generated by Django 3.2 on 2021-06-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_user_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
