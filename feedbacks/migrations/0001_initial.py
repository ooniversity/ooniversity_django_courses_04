# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f')),
                ('subject', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('message', models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('from_email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('create_date', models.DateTimeField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
