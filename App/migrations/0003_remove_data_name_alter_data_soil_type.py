# Generated by Django 4.2.7 on 2023-11-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_data_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='name',
        ),
        migrations.AlterField(
            model_name='data',
            name='soil_type',
            field=models.PositiveIntegerField(choices=[(0, 'Clay'), (1, 'Silt'), (2, 'Sandy'), (3, 'Loam'), (4, 'Rocky')], null=True),
        ),
    ]