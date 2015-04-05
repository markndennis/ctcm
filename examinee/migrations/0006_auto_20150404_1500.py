# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0005_examinee_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinee',
            name='approved',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
