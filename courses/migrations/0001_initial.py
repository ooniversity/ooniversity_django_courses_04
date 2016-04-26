# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('short_description', models.CharField(max_length=1000, verbose_name='Short description')),
                ('description', models.TextField(verbose_name='Description')),
                ('assistant', models.ForeignKey(related_name='assistant_courses', blank=True, to='coaches.Coach', null=True)),
                ('coach', models.ForeignKey(related_name='coach_courses', blank=True, to='coaches.Coach', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('description', models.TextField(verbose_name='Description')),
                ('order', models.PositiveIntegerField(verbose_name='Order')),
                ('course', models.ForeignKey(verbose_name='Courses', to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
