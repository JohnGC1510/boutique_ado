# Generated by Django 3.2 on 2021-04-22 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210422_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaulttown_or_city',
            new_name='default_town_or_city',
        ),
    ]
