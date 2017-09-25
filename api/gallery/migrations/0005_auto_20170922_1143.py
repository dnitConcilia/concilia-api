# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-22 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20170922_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='face',
            field=models.ImageField(upload_to='gallery/faces', verbose_name='Rosto da galeria'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='gallery/photos', verbose_name='Arquivo'),
        ),
    ]