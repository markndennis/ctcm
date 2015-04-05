# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invigilator', '0002_auto_20150402_1542'),
        ('examinee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinee',
            name='invigilator',
            field=models.ForeignKey(default=2, to='invigilator.Invigilator'),
            preserve_default=False,
        ),
    ]
