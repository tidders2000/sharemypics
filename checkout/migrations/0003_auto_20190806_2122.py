# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-06 21:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0002_orderlineitem_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='seller',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='buyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
