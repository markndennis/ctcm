# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0006_auto_20150404_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinee',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
