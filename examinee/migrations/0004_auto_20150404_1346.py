# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0003_remove_examinee_exam_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinee',
            name='dob',
            field=models.DateField(default='2001-01-01', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examinee',
            name='exam_type',
            field=models.ForeignKey(default=1, to='examinee.ExamType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examinee',
            name='intended',
            field=models.DateField(default='2001-01-01', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examinee',
            name='regnum',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
