# Generated by Django 3.2.2 on 2022-04-04 13:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220404_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 4, 13, 28, 48, 177621, tzinfo=utc)),
        ),
    ]
