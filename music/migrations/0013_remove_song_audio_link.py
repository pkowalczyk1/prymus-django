# Generated by Django 3.2.6 on 2021-09-21 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_song_audio_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_link',
        ),
    ]