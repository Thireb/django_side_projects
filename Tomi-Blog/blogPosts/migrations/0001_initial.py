# Generated by Django 4.0.2 on 2022-07-15 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=5000)),
                ('creation_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
