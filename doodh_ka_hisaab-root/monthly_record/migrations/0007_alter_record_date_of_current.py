# Generated by Django 3.2.2 on 2021-06-17 12:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_record', '0006_alter_record_date_of_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Date_of_Current',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 12, 8, 14, 190369, tzinfo=utc), verbose_name='Last Added'),
        ),
    ]
