# Generated by Django 3.2.2 on 2021-06-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.DecimalField(decimal_places=2, default=3, max_digits=5)),
                ('Date_of_Current', models.DateField()),
            ],
        ),
    ]
