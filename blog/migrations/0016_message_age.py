# Generated by Django 4.2.4 on 2023-11-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_message_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
