# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CusPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='cus_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('info', models.TextField()),
            ],
        ),
    ]
