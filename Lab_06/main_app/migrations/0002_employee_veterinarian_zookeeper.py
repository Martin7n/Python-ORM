# Generated by Django 5.0.4 on 2024-07-10 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinarian',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.employee')),
                ('license_number', models.CharField(max_length=10)),
            ],
            bases=('main_app.employee',),
        ),
        migrations.CreateModel(
            name='ZooKeeper',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.employee')),
                ('specialty', models.CharField(choices=[('Mammals', 'Mammals'), ('Birds', 'Birds'), ('Reptiles', 'Reptiles'), ('Others', 'Others')], max_length=10)),
                ('managed_animals', models.ManyToManyField(to='main_app.animal')),
            ],
            bases=('main_app.employee',),
        ),
    ]
