# Generated by Django 4.0.5 on 2022-07-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0006_remove_order_provinsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='provinsi',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
