# Generated by Django 3.0 on 2020-01-10 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20200110_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='time_of_message',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='work_exp',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 15, 29, 38, 913455), null=True),
        ),
    ]