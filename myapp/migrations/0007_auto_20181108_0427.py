# Generated by Django 2.1.3 on 2018-11-08 04:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20181106_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 8, 4, 27, 51, 166501, tzinfo=utc)),
        ),
    ]
