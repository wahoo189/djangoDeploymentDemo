# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaseballLeague(models.Model):
    name = models.CharField(max_length=38)
    leagueClass = models.CharField(max_length=38)
    region = models.CharField(max_length=38)

class BaseballTeam(models.Model):
    city = models.CharField(max_length=38)
    team_name = models.CharField(max_length= 38)
    mascot = models.CharField(max_length= 38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    league = models.ManyToManyField(BaseballLeague, related_name="team")

class BaseballPlayer(models.Model):
    name = models.CharField(max_length=38)
    position = models.CharField(max_length= 38)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(BaseballTeam, related_name="player")

# class BaseballGame(models.Model):
#     books = models.ManyToManyField(Book, related_name="publishers")
#     name = models.CharField(max_length=38)
#     position = models.CharField(max_length= 38)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

