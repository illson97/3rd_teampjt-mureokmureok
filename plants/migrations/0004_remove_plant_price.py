# Generated by Django 3.2.18 on 2023-06-05 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_plant_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='price',
        ),
    ]
