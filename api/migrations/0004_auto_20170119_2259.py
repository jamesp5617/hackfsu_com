# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 22:59
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20161206_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('comments', models.CharField(blank=True, default='', max_length=1000)),
                ('misc_info', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
                ('affiliation', models.CharField(max_length=100)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hackathon')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='hackerinfo',
            name='agreed_to_mlh_data_sharing',
        ),
        migrations.RemoveField(
            model_name='hackerinfo',
            name='school_name',
        ),
        migrations.RemoveField(
            model_name='school',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='waiver_signature',
        ),
        migrations.AddField(
            model_name='hackerinfo',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hackerinfo',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='hackerinfo',
            name='misc_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='hackerinfo',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.School'),
        ),
        migrations.AddField(
            model_name='judgeinfo',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='judgeinfo',
            name='misc_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='hackathon',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Hackathon'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='misc_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='url',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='school',
            name='user_submitted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]