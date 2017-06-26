from django.conf.urls import url
from . import views           # So we can call functions from our routes!

urlpatterns = [
	# url(r'^$', views.index),       # 'home' route.
	# url(r'^(?P<id>\d+)$', views.index),
	# url(r'^(?P<id>\w+)$', views.index),

	# for Models demo
	url(r'^modelsDemo$', views.modelsDemo),

	# cRud
	url(r'^teams$', views.listTeams, name="standings"),
	url(r'^players$', views.listPlayers, name="rosters"),

	# Crud
	url(r'^createTeam$', views.createTeam, name="makeTeam"),
	url(r'^createPlayer$', views.createPlayer, name="makePlayer"),
	
	# cruD
	url(r'^deleteAllPlayers$', views.deletePlayers, name="tradeTeam"),
	url(r'^deleteAllTeams$', views.deleteTeams, name="exitLeague"),
	url(r'^deletePlayer/(?P<id>\d+)$', views.deletePlayer, name="demotePlayer"),
	
	# crUd
	url(r'^editPlayer/(?P<id>\d+)$', views.editPlayer, name="stats"),
	url(r'^updatePlayer$', views.updatePlayer, name="trackPlayer")
]