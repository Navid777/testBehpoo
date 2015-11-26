# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0002_fsmchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='viewflow.Process', parent_link=True)),
                ('text', models.CharField(max_length=200)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
