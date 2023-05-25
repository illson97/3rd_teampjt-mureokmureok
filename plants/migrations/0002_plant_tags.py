# Generated by Django 3.2.18 on 2023-05-25 02:16

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
