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
                ('name', models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f')),
                ('surname', models.CharField(max_length=255, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('date_of_birth', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('address', models.CharField(max_length=255, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('skype', models.CharField(max_length=255)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
