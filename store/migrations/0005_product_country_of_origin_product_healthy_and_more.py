# Generated by Django 5.1.2 on 2024-10-21 12:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country_of_origin',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='healthy',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='quality',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]