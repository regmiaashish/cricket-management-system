# Generated by Django 5.1.4 on 2025-02-01 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0027_alter_team_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='venue',
        ),
    ]
