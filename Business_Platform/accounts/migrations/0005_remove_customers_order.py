# Generated by Django 4.1.7 on 2023-02-24 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customers_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='order',
        ),
    ]
