# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='fist_name',
            field=models.CharField(default=b'First Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='agent',
            name='last_name',
            field=models.CharField(default=b'Last Name', max_length=50),
        ),
    ]
