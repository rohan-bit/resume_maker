# Generated by Django 3.0 on 2019-12-27 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20191227_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
                ('projects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
    ]
