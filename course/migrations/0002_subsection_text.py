# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsection',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
