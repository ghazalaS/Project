# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-27 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0013_auto_20160926_0508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerrating',
            old_name='user',
            new_name='c_username',
        ),
        migrations.RenameField(
            model_name='favourites',
            old_name='user',
            new_name='c_username',
        ),
        migrations.RenameField(
            model_name='favourites',
            old_name='repairer_id',
            new_name='r_username',
        ),
    ]