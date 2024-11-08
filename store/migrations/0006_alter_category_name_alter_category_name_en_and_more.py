# Generated by Django 5.1.2 on 2024-11-08 16:28

import django.core.validators
import store.models
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_category_name_en_category_name_ka_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ka',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='country_of_origin',
            field=models.CharField(max_length=100, verbose_name='Country_of_origin'),
        ),
        migrations.AlterField(
            model_name='product',
            name='country_of_origin_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Country_of_origin'),
        ),
        migrations.AlterField(
            model_name='product',
            name='country_of_origin_ka',
            field=models.CharField(max_length=100, null=True, verbose_name='Country_of_origin'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='healthy',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='healthy_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='healthy_ka',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=store.models.generate_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='quality',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='quality_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quality_ka',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
