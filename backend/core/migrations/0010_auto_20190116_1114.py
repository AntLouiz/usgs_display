# Generated by Django 2.1.5 on 2019-01-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_raster_download_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raster',
            name='download_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]