# Generated by Django 5.0.4 on 2024-06-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_smartphone_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('customer_name', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('CO', 'Completed'), ('CA', 'CANCELLED')], default='Pending', max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('warranty', models.CharField(default='No warranty', max_length=100)),
                ('delivery', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
