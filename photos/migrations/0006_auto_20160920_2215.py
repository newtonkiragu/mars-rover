# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_photo_next_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='rover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photos.Rover'),
        ),
    ]