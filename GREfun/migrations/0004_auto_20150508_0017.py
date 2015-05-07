# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('GREfun', '0003_auto_20150508_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(related_name='student_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
