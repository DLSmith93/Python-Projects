# Generated by Django 5.0.1 on 2024-01-14 22:11

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=60)),
                ('campusID', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'University Campuses',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
