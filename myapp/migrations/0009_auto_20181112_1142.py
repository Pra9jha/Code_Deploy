# Generated by Django 2.1.3 on 2018-11-12 11:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20181112_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 12, 11, 42, 10, 191409, tzinfo=utc)),
        ),
    ]
