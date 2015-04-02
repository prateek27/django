# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
        migrations.RemoveField(
            model_name='comments',
            name='by',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='by',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='has_tags',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='likers',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='user_tags',
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(to='photo.Photo'),
            preserve_default=True,
        ),
    ]
