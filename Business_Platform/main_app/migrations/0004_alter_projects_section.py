# Generated by Django 4.1.7 on 2023-02-21 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_section_section_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.section'),
        ),
    ]
