# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-27 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverinfo',
            name='checkflag',
            field=models.CharField(blank=True, choices=[('0', '\u5426'), ('1', '\u662f')], max_length=2, verbose_name='\u662f\u5426\u76d1\u63a7'),
        ),
    ]
