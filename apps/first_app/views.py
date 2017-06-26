# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse

from .models import BaseballTeam, BaseballPlayer

# Create your views here.

def index(request, id):
    
    context = {
        'routeID': id,
        'userInfo': 'This is some information about the user, arbitrary, for now.',        
    }

    return render(request, "first_app/index.html", context)

def modelsDemo(request):
    
    return render(request, "first_app/modelsDemo.html")

def listPlayers(request):
    context = {
        'players' : BaseballPlayer.objects.all()
    }
    return render(request, "first_app/players.html", context)

def listTeams(request):
    context = {
        'teams' : BaseballTeam.objects.all()
    }
    return render(request, "first_app/teams.html", context)

def createTeam(request):
    BaseballTeam.objects.create(city=request.POST['city'],team_name=request.POST['teamName'], mascot=request.POST['mascot'])
    return redirect("/teams")

def createPlayer(request):
    BaseballPlayer.objects.create(name=request.POST['name'],position=request.POST['position'], salary=request.POST['salary'])
    return redirect("/players")
    # return redirect("{% url 'rosters' %}")
    # return redirect(reverse("BaseballUniverse:rosters"))

def deleteTeams(request):
    BaseballTeam.objects.all().delete()
    return redirect("/teams")
    
def deletePlayers(request):
    BaseballPlayer.objects.all().delete()
    return redirect("/players")
    
def deletePlayer(request, id):
    # actuall delete the player
    result = BaseballPlayer.objects.get(id=id).delete()
    print result
    print "The player with the id of", id, " has been sent down to the minors."
    return redirect("/players")

def editPlayer(request, id):
    
    context = {
        'player' : BaseballPlayer.objects.get(id=id)
    }

    return render(request, "first_app/editPlayer.html", context)

def updatePlayer(request):

    player = BaseballPlayer.objects.get(id=request.POST['player_id']) 
    player.name = request.POST['name']
    player.salary = request.POST['salary']
    player.position = request.POST['position']
    player.save()
       

    return redirect("/players")
    
    








