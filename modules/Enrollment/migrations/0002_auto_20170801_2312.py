# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=200),
        ),
    ]