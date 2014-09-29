# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('brief', tinymce.models.HTMLField(null=True, blank=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('client', models.ForeignKey(blank=True, to='client.Client', null=True)),
                ('responsible', models.ManyToManyField(related_name=b'project_responsible', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
