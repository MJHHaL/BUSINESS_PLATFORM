# Generated by Django 4.1.7 on 2023-02-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_remove_orders_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='send_to',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
