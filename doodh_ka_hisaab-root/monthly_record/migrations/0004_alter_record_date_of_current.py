# Generated by Django 3.2.2 on 2021-06-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_record', '0003_alter_record_date_of_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Date_of_Current',
            field=models.DateField(auto_now_add=True, verbose_name='Last Added'),
        ),
    ]