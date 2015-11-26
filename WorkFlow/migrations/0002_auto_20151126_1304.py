# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0002_fsmchange'),
        ('WorkFlow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='viewflow.Process', auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
        migrations.RemoveField(
            model_name='testprocess',
            name='process_ptr',
        ),
        migrations.DeleteModel(
            name='TestProcess',
        ),
    ]
