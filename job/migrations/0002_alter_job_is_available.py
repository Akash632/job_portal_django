# Generated by Django 5.0.1 on 2024-03-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
