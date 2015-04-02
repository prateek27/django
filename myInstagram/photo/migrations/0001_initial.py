# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('photo_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to='uploads/')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=300, null=True)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='photos')),
                ('has_tags', models.ManyToManyField(to='photo.HashTag')),
                ('likers', models.ManyToManyField(related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('user_tags', models.ManyToManyField(related_name='tagged_in', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comments',
            name='photo',
            field=models.ForeignKey(to='photo.Photos'),
            preserve_default=True,
        ),
    ]
