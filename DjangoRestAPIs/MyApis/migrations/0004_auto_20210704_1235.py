# Generated by Django 3.0 on 2021-07-04 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApis', '0003_auto_20210704_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 4, 7, 5, 46, 645787)),
        ),
    ]
