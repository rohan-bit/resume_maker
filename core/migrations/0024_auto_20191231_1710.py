# Generated by Django 3.0 on 2019-12-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20191228_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='position_of_reponsiblity',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='position_of_reponsiblity',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
