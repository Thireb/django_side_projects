# Generated by Django 4.1.3 on 2022-11-10 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('jawab', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=20)),
                ('submitted', models.DateField(auto_now_add=True)),
                ('money', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('jobfile', models.FileField(blank=True, upload_to='Uploads/')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
