# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-21 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='answered',
            field=models.BooleanField(default=False, verbose_name='Respondido'),
        ),
    ]
