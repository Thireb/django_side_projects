# Generated by Django 3.2.10 on 2022-01-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female'), ('TRANSGENDER', 'transgender')], max_length=50)),
                ('blood_group', models.CharField(choices=[('A-POSITIVE', 'A+'), ('A-NEGATIVE', 'A-'), ('B-POSITIVE', 'B+'), ('B-NEGATIVE', 'B-'), ('AB-POSTITVE', 'AB+'), ('AB-NEGATIVE', 'AB-'), ('O-POSITIVE', 'O+'), ('O-NEGATIVE', 'O-')], max_length=50)),
                ('contact', models.PositiveSmallIntegerField(max_length=11, verbose_name='Enter your phone number, 11 digits only.')),
                ('cnic', models.PositiveSmallIntegerField(max_length=13, verbose_name='Enter your CNIC.')),
                ('address', models.TextField()),
            ],
        ),
    ]
