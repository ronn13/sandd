# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2009-01-01 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_names', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shampoo', models.IntegerField()),
                ('hairgel', models.IntegerField()),
                ('relaxer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=250)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Agent')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Store'),
        ),
    ]
