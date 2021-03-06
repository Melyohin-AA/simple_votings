# Generated by Django 3.0.1 on 2020-02-01 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200201_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='voting',
            name='date_started',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='voting',
            name='date_stopped',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
