# Generated by Django 3.0 on 2019-12-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ManyToManyField(to='core.Profile'),
        ),
    ]
