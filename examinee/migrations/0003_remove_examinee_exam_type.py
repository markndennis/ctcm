# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0002_examinee_invigilator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examinee',
            name='exam_type',
        ),
    ]
