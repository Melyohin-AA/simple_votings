# Generated by Django 3.0.1 on 2020-02-01 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200201_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 1, 15, 35, 49, 87964)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='date_started',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 1, 15, 35, 49, 87964)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='date_stopped',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 1, 15, 35, 49, 87964)),
        ),
    ]
