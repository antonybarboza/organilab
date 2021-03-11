# Generated by Django 2.2.13 on 2020-10-09 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0017_auto_20201005_1241'),
        ('reservations_management', '0011_auto_20201007_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservedproducts',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Requested'), (1, 'Borrowed'), (2, 'Denied'), (4, 'Returned')], default=0),
        ),
        migrations.CreateModel(
            name='SelectedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_required', models.FloatField()),
                ('initial_date', models.DateTimeField()),
                ('final_date', models.DateTimeField()),
                ('shelf_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.ShelfObject')),
            ],
        ),
    ]
