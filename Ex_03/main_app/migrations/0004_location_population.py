# Generated by Django 5.0.4 on 2024-07-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='population',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
