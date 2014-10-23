# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.FloatField(default=0.0)),
                ('image', models.ImageField(upload_to=b'prod_images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
