# Generated by Django 4.1.7 on 2023-03-01 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_remove_projects_rating_comments_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.projects'),
        ),
    ]
