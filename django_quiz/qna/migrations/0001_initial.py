# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('category_tags', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_options', models.IntegerField(verbose_name=False)),
                ('options', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_identifier', models.CharField(max_length=255)),
                ('question_text', models.TextField()),
                ('question_tags', models.CharField(max_length=255)),
                ('question_category', models.ManyToManyField(to='qna.Category')),
            ],
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qna.Question'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qna.Question'),
        ),
    ]
