# Generated by Django 3.2 on 2021-04-22 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaultphone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('defaultcountry', django_countries.fields.CountryField(max_length=2)),
                ('defaultpostcode', models.CharField(blank=True, max_length=20, null=True)),
                ('defaulttown_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('defaultstreet_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('defaultstreet_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('defaultcounty', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]