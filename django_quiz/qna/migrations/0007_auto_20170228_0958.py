# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-28 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0006_auto_20170228_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='option10',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='option3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='option4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='option5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='option6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='option7',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='option8',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='option9',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
