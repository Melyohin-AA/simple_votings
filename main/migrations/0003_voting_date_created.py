# Generated by Django 3.0.2 on 2020-01-09 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200107_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 9, 8, 32, 11, 411842)),
        ),
    ]
