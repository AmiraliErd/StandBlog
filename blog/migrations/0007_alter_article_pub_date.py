# Generated by Django 4.2.4 on 2023-10-05 20:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_article_description_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 5, 20, 45, 16, 515260, tzinfo=datetime.timezone.utc)),
        ),
    ]