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
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('skype', models.CharField(max_length=50, verbose_name='Skype')),
                ('courses', models.ManyToManyField(to='courses.Course', verbose_name='Courses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
