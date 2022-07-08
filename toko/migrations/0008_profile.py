# Generated by Django 4.0.5 on 2022-07-08 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toko', '0007_order_provinsi_alter_order_payment_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('alamat', models.CharField(max_length=150)),
                ('kota', models.CharField(max_length=150)),
                ('provinsi', models.CharField(blank=True, max_length=150)),
                ('kode_pos', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
