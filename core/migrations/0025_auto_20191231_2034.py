# Generated by Django 3.0 on 2019-12-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20191231_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position_of_reponsiblity',
            name='positon',
            field=models.CharField(max_length=255),
        ),
    ]