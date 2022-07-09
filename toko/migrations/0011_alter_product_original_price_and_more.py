# Generated by Django 4.0.5 on 2022-07-09 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0010_alter_product_original_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]