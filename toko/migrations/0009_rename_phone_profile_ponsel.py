# Generated by Django 4.0.5 on 2022-07-08 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0008_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='ponsel',
        ),
    ]
