# Generated by Django 3.1.5 on 2021-04-19 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0016_auto_20210419_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytuber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 13, 48, 21, 55881)),
        ),
    ]