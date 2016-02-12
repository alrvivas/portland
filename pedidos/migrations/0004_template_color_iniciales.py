# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_remove_template_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='color_iniciales',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
