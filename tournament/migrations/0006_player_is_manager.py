# Generated by Django 5.1.4 on 2025-01-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_player_description_alter_player_batting_style_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
