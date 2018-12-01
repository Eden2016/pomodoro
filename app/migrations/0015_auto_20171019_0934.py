# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-19 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20170118_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('answered', 'Answered'), ('rejected', 'Rejected'), ('duplicate', 'Duplicate')], default='new', max_length=100, verbose_name='Status'),
        ),
    ]
