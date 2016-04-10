# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quardatic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a', models.IntegerField(default=None)),
                ('b', models.IntegerField(default=None)),
                ('c', models.IntegerField(default=None)),
                ('d', models.IntegerField(default=None)),
                ('x1', models.IntegerField(default=None)),
                ('x2', models.IntegerField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
