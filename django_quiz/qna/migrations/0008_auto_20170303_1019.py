# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-03 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0007_auto_20170228_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.upload_to),
        ),
        migrations.AlterField(
            model_name='answers',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qna.Question'),
        ),
        migrations.AlterField(
            model_name='options',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='qna.Question'),
        ),
    ]
