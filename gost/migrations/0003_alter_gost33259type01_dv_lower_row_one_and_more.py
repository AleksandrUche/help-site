# Generated by Django 4.1.3 on 2023-12-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gost', '0002_alter_gost28759flangemass_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gost33259type01',
            name='dv_lower_row_one',
            field=models.CharField(blank=True, max_length=20, verbose_name='dв'),
        ),
        migrations.AlterField(
            model_name='gost33259type01',
            name='dv_lower_row_two',
            field=models.CharField(blank=True, max_length=20, verbose_name='dв'),
        ),
        migrations.AlterField(
            model_name='gost33259type02',
            name='d0_row_one',
            field=models.CharField(blank=True, max_length=20, verbose_name='D0'),
        ),
        migrations.AlterField(
            model_name='gost33259type02',
            name='d0_row_two',
            field=models.CharField(blank=True, max_length=20, verbose_name='D0'),
        ),
        migrations.AlterField(
            model_name='gost33259type02',
            name='dv_lower_row_one',
            field=models.CharField(blank=True, max_length=20, verbose_name='dв'),
        ),
        migrations.AlterField(
            model_name='gost33259type02',
            name='dv_lower_row_two',
            field=models.CharField(blank=True, max_length=20, verbose_name='dв'),
        ),
    ]
