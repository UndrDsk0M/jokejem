# Generated by Django 5.0.6 on 2024-08-29 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_keywords_item_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='emojie_1',
            field=models.CharField(default='💰', max_length=5),
        ),
        migrations.AddField(
            model_name='item',
            name='emojie_2',
            field=models.CharField(default='💵', max_length=5),
        ),
    ]
