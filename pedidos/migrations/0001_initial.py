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
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.DecimalField(default=False, max_digits=4, decimal_places=2, blank=True)),
                ('pagado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField(null=True)),
                ('direccion', models.CharField(max_length=140, null=True)),
                ('titulo_principal', models.CharField(max_length=100, null=True)),
                ('color_titulo', models.CharField(max_length=25, null=True)),
                ('iniciales', models.CharField(max_length=10, null=True)),
                ('boton_1', models.CharField(max_length=25, null=True)),
                ('boton_2', models.CharField(max_length=25, null=True)),
                ('boton_3', models.CharField(max_length=25, null=True)),
                ('background', models.ImageField(default=b'images/background/default-01.png', upload_to=b'images/background', null=True, verbose_name=b'Imagen Fondo', blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='template',
            field=models.OneToOneField(null=True, blank=True, to='pedidos.Template'),
        ),
    ]
