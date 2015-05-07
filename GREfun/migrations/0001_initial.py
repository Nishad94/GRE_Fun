# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meaning_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_text', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='choice1',
            field=models.ForeignKey(related_name='question_c1', to='GREfun.Word'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='choice2',
            field=models.ForeignKey(related_name='question_c2', to='GREfun.Word'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='choice3',
            field=models.ForeignKey(related_name='question_c3', to='GREfun.Word'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='meaning',
            field=models.ForeignKey(to='GREfun.Meaning'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meaning',
            name='word',
            field=models.ForeignKey(to='GREfun.Word'),
            preserve_default=True,
        ),
    ]
