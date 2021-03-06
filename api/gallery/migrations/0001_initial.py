# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-26 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria')),
                ('subCategory', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subcategoria')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Categoria da notícia',
                'verbose_name_plural': 'Categorias das notícias',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Título')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Texto')),
                ('slug', models.SlugField(help_text="'slug' é um identificador único que será mostrado na url", max_length=500, unique=True, verbose_name='Slug')),
                ('is_public', models.BooleanField(default=True, help_text='Somente as notícias marcadas como públicas serão apresentadas no site.', verbose_name='É Pública ?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('categoryGallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.CategoryGallery')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('photo', models.ImageField(upload_to='/gallery/photos', verbose_name='Arquivo')),
                ('legend', models.CharField(blank=True, max_length=300, verbose_name='Legenda')),
                ('credit', models.CharField(blank=True, max_length=100, verbose_name='Créditos')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link externo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('embed', models.TextField(verbose_name='Código do youtube')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='photos',
            field=models.ManyToManyField(to='gallery.Photo'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='videos',
            field=models.ManyToManyField(to='gallery.Video'),
        ),
    ]
