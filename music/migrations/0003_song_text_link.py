# Generated by Django 3.2.6 on 2021-08-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210822_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='text_link',
            field=models.CharField(default='No link', max_length=150),
        ),
    ]
