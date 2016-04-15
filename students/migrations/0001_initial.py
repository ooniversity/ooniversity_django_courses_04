# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='\u0418\u043c\u044f:')),
                ('surname', models.CharField(max_length=150, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('date_of_birth', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('email', models.EmailField(max_length=75, verbose_name='Mail')),
                ('phone', models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b.')),
                ('address', models.CharField(max_length=250, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('skype', models.CharField(max_length=60, verbose_name='Skype')),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
