# Generated by Django 2.2.12 on 2020-06-11 03:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msds', '0002_auto_20200525_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msdsobject',
            name='file',
            field=models.FileField(upload_to='msds', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='MSDS File'),
        ),
    ]
