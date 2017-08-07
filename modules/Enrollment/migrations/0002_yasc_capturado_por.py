# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 01:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yasc',
            name='capturado_por',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
