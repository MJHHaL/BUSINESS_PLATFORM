# Generated by Django 4.1.7 on 2023-02-27 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customers'),
        ('main_app', '0009_rename_order_name_backlog_order_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='customer_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.customers'),
        ),
    ]
