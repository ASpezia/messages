# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-27 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20180427_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='others_messages',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='first_app.User'),
        ),
    ]
