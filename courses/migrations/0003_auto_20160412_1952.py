# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160412_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.PositiveIntegerField(blank=True),

        ),
    ]
