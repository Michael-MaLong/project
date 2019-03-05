# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-27 08:40
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSetinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absname', models.CharField(max_length=300, verbose_name='\u76d1\u63a7\u8d44\u6e90\u8def\u5f84')),
                ('writetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u548c\u76d1\u63a7\u8d44\u6e90\u5bf9\u5e94\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Serverinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u670d\u52a1\u5668\u540d\u79f0')),
                ('ip', models.CharField(max_length=100, verbose_name='IP')),
                ('port', models.CharField(max_length=100, verbose_name='\u7aef\u53e3')),
                ('username', models.CharField(max_length=100, verbose_name='\u7528\u6237\u540d\u79f0')),
                ('password', models.CharField(max_length=100, verbose_name='\u7528\u6237\u5bc6\u7801')),
                ('writetime', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('synctime', models.DateTimeField(blank=True, null=True, verbose_name='\u540c\u6b65\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u4fe1\u606f',
            },
        ),
        migrations.AlterUniqueTogether(
            name='serverinfo',
            unique_together=set([('ip',)]),
        ),
        migrations.AlterIndexTogether(
            name='serverinfo',
            index_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='contentsetinfo',
            name='serverid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serverinfo.Serverinfo', verbose_name='\u76d1\u63a7\u670d\u52a1\u5668'),
        ),
        migrations.AddField(
            model_name='contentsetinfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
        migrations.AlterUniqueTogether(
            name='contentsetinfo',
            unique_together=set([('serverid', 'absname', 'user')]),
        ),
    ]
