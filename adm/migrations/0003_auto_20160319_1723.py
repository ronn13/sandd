# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_products_stock_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('stock_type', models.CharField(choices=[(1, b'Opening Stock'), (2, b'Closing stock'), (3, b'New stock')], max_length=20)),
                ('stock_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='products',
            old_name='hairgel',
            new_name='unit_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='relaxer',
        ),
        migrations.RemoveField(
            model_name='products',
            name='shampoo',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock_type',
        ),
        migrations.RemoveField(
            model_name='products',
            name='store',
        ),
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(default=b'product', max_length=20),
        ),
        migrations.AddField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Products'),
        ),
        migrations.AddField(
            model_name='stock',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Store'),
        ),
    ]
