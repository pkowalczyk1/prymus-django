# Generated by Django 3.2.6 on 2021-08-28 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20210828_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('is_recommended', models.BooleanField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song')),
            ],
            options={
                'verbose_name': 'recenzja',
                'verbose_name_plural': 'recenzje',
            },
        ),
    ]