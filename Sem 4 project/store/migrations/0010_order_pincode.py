# Generated by Django 3.2 on 2021-06-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210619_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
