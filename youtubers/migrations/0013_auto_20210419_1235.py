# Generated by Django 3.1.5 on 2021-04-19 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0012_auto_20210419_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytuber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 12, 35, 21, 967738)),
        ),
    ]
