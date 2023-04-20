# Generated by Django 4.2 on 2023-04-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popular_women', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
