# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_of_following', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('profile_pic', models.ImageField(upload_to='/profile_pics', blank=True)),
                ('phone_number', models.CharField(unique=True, max_length=10)),
                ('city', models.ForeignKey(to='account.City')),
                ('following_user', models.ManyToManyField(related_name='followers', to='account.UserProfile', through='account.Following')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='following',
            name='by',
            field=models.ForeignKey(related_name='follower', to='account.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='following',
            name='to',
            field=models.ForeignKey(related_name='followee', to='account.UserProfile'),
            preserve_default=True,
        ),
    ]
