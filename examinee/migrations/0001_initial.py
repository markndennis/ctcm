# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
        ('invigilator', '0006_auto_20150404_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examinee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('regnum', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('dob', models.DateField(blank=True)),
                ('intended', models.DateField(blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('exam_type', models.ForeignKey(to='exams.ExamType')),
                ('invigilator', models.ForeignKey(to='invigilator.Invigilator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
