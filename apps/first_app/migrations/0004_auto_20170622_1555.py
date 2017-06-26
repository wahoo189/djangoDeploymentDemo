# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-22 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20170620_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseballLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=38)),
                ('leagueClass', models.CharField(max_length=38)),
                ('region', models.CharField(max_length=38)),
            ],
        ),
        migrations.DeleteModel(
            name='BaseballGame',
        ),
        migrations.AddField(
            model_name='baseballplayer',
            name='team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='first_app.BaseballTeam'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baseballteam',
            name='league',
            field=models.ManyToManyField(related_name='team', to='first_app.BaseballLeague'),
        ),
    ]