# Generated by Django 2.2.13 on 2020-10-05 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0004_reservedproducts_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationtasks',
            old_name='celery_task_id',
            new_name='celery_task',
        ),
        migrations.RenameField(
            model_name='reservedproducts',
            old_name='shelf_object_id',
            new_name='shelf_object',
        ),
    ]
