# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-21 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorygallery',
            options={'verbose_name': 'Categoria da galeria', 'verbose_name_plural': 'Categorias das galerias'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Galeria', 'verbose_name_plural': 'Galerias'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
    ]
