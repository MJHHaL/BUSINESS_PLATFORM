# Generated by Django 4.1.7 on 2023-03-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_github_profile_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, default='github.com', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, default='twitter.com', max_length=100, null=True),
        ),
    ]