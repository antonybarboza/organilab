# Generated by Django 4.0.8 on 2022-11-06 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0055_commentinform_inform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationusermanagement',
            name='group',
        ),
    ]