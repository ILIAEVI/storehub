# Generated by Django 5.1.2 on 2024-10-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_country_of_origin_product_healthy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='country_of_origin',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='healthy',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='quality',
            field=models.CharField(max_length=100),
        ),
    ]