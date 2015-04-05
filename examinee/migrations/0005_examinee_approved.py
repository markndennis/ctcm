# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0004_auto_20150404_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinee',
            name='approved',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
