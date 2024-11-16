# Generated by Django 5.0.6 on 2024-08-28 16:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_emojie'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='keywords',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='keywords',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]