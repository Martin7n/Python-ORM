# Generated by Django 5.0.4 on 2024-06-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
