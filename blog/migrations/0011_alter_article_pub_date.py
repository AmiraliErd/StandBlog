# Generated by Django 4.2.4 on 2023-10-23 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_slug_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 23, 14, 20, 41, 676335, tzinfo=datetime.timezone.utc)),
        ),
    ]
