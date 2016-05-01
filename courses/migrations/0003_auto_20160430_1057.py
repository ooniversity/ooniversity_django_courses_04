# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160417_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
