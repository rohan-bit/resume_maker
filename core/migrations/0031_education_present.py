# Generated by Django 3.0 on 2020-01-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_work_exp_company_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
