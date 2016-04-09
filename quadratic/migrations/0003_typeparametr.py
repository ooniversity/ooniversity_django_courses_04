# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadratic', '0002_solution'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeParametr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_a', models.CharField(max_length=200)),
                ('char_b', models.CharField(max_length=200)),
                ('char_c', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
