# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-27 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0003_auto_20171017_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo de edital')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Tipo de edital',
                'verbose_name_plural': 'Tipos de editais',
            },
        ),
        migrations.AlterField(
            model_name='notice',
            name='noticeType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meeting.NoticeType'),
        ),
    ]