# Generated by Django 4.1 on 2022-09-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='time_stamp',
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
