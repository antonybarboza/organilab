# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-07 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msds', '0009_auto_20190423_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegulationDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('file', models.FileField(upload_to='regulation/', verbose_name='Regulation File')),
                ('country', models.CharField(max_length=50)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Regulation document',
                'verbose_name_plural': 'Regulation documents',
                'ordering': ('order',),
            },
        ),
    ]