# Generated by Django 4.2.4 on 2023-12-18 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_prifile_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'حساب کاربری', 'verbose_name_plural': 'حساب های کاربری'},
        ),
    ]
