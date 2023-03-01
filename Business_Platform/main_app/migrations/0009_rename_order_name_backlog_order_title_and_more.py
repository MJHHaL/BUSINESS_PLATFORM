# Generated by Django 4.1.7 on 2023-02-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customers'),
        ('main_app', '0008_backlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backlog',
            old_name='order_name',
            new_name='order_title',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='user',
        ),
        migrations.AddField(
            model_name='backlog',
            name='customer_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.customers'),
        ),
    ]