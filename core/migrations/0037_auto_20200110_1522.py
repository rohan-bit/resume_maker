# Generated by Django 3.0 on 2020-01-10 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20200110_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='time_of_message',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 15, 22, 15, 921452)),
        ),
        migrations.AlterField(
            model_name='work_exp',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 15, 22, 15, 917391), null=True),
        ),
    ]
