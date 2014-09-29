# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(default=b'QUOTE', max_length=10, choices=[(b'QUOTE', b'Forslag'), (b'INVOICE', b'Faktura')])),
                ('client', models.ForeignKey(blank=True, to='client.Client', null=True)),
                ('project', models.ForeignKey(blank=True, to='project.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuoteLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('quote', models.ForeignKey(to='quote.Quote')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
