# Generated by Django 4.1.7 on 2023-02-24 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('accounts', '0003_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.orders'),
        ),
    ]
