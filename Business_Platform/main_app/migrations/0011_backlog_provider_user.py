# Generated by Django 4.1.7 on 2023-02-28 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customers'),
        ('main_app', '0010_alter_backlog_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlog',
            name='provider_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.provider'),
        ),
    ]
