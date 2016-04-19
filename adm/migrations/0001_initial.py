# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('fist_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'product name', max_length=20)),
                ('unit_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_count', models.IntegerField()),
                ('stock_type', models.CharField(max_length=20, choices=[(b'1', b'Opening Stock'), (b'2', b'Closing stock'), (b'3', b'New stock')])),
                ('stock_time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(to='adm.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=250)),
                ('agent', models.ForeignKey(to='adm.Agent')),
                ('store_location', models.ForeignKey(to='adm.Location')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='store',
            field=models.ForeignKey(to='adm.Store'),
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(to='adm.Region'),
        ),
    ]
