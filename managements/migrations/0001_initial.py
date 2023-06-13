# Generated by Django 3.2.18 on 2023-06-13 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import managements.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0002_plant_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('nickname', models.CharField(max_length=20)),
                ('managementdate', models.DateField(null=True)),
                ('photo', models.ImageField(upload_to=managements.models.management_img_path)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CalenderEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watering', models.CharField(max_length=20)),
                ('sunlight', models.CharField(max_length=20)),
                ('humidity', models.CharField(max_length=20)),
                ('things', models.CharField(max_length=20)),
                ('significant', models.CharField(max_length=40)),
                ('temperature', models.CharField(max_length=20)),
                ('entrydate', models.DateField(null=True)),
                ('management', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.management')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
