# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='img_id',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img_id',
        ),
        migrations.AlterField(
            model_name='album',
            name='published',
            field=models.CharField(choices=[('PRI', 'private'), ('SHA', 'shared'), ('PUB', 'public')], default='PRI', max_length=3),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
