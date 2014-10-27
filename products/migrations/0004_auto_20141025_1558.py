# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20141025_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(default='', to='products.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='itemtype',
            field=models.ForeignKey(default='', to='products.ItemType'),
            preserve_default=False,
        ),
    ]
