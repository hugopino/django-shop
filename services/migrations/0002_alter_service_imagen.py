# Generated by Django 4.1.5 on 2023-01-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='imagen',
            field=models.ImageField(upload_to='services'),
        ),
    ]
