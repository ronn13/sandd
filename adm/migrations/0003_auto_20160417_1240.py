# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20160417_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='username',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
