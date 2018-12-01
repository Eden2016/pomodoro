# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-02 08:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='pomodoro_duration',
            field=models.DurationField(default=datetime.timedelta(0, 1500)),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0, 1500)),
        ),
    ]
