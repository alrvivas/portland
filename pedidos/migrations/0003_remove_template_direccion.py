# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20160210_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='direccion',
        ),
    ]
