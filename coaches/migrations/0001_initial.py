# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
                ('gender', models.CharField(max_length=1, verbose_name='Sex', choices=[('M', 'Male'), ('F', 'Female')])),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('skype', models.CharField(max_length=50, verbose_name='Skype')),
                ('description', models.TextField(verbose_name='Description')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
