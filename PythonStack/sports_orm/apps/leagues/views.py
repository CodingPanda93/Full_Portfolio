from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	#...all baseball leagues
	query1 = League.objects.filter(sport='Baseball')
	#...all womens' leagues
	query2 = League.objects.filter(name__contains="Women's")
	#...all leagues where sport is any type of hockey
	query3 = League.objects.filter(sport='hockey')
	#...all leagues that call themselves "conferences"
	query4 = League.objects.filter(name__contains='conferences')
	#...all leagues in the Atlantic region
	query5 = Team.objects.filter(location='Atlantic')
	#...all teams based in Dallas
	query6 = Team.objects.filter(location='Dallas')
	#...all teams named the Raptors
	query7 = Team.objects.filter(team_name__contains='Raptors')
	#...all teams whose location includes "City"
	query8 = Team.objects.filter(location__contains='City')
	#...all teams whose names begin with "T"
	query9 = Team.objects.filter(team_name__startswith='T')
	#...all teams, ordered alphabetically by location
	query10 = Team.objects.all().order_by('team_name')
	#...all teams, ordered by team name in reverse alphabetical order
	query11 = Team.objects.all().order_by('team_name').reverse()
	#...every player with last name "Cooper"
	query12 = Player.objects.filter(last_name='Cooper')
	#...every player with first name "Joshua"
	query13 = Player.objects.filter(first_name='Joshua')
	#...every player with last name "Cooper" EXCEPT FOR Joshua
	query14 = Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')
	#...all players with first name "Alexander" OR first name "Wyatt"
	query15 = Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt')
	context = {
		'leagues': League.objects.all(),
		'teams': Team.objects.all(),
		'players': Player.objects.all(),
		'all_baseball': query1,
		'women_league': query2,
		'hockey': query3,
		'conferences': query4,
		'atlantic': query5,
		'dallas':query6,
		'raptors': query7,
		'city': query8,
		't_teams': query9,
		'teams1': query10,
		'teams2': query11,
		'cooper': query12,
		'joshua': query13,
		'cooper_joshua': query14,
		'alexander_wyatt': query15,
	}
	return render(request, "leagues/index.html", context)

def sport_orm2(request):
	#...all teams in the Atlantic Soccer Conference
	query16 = Team.objects.filter(league=League.objects.get(name='Atlantic Soccer Conference'))
	#...all (current) players on the Boston Penguins
	##come back
	#...all (current) players in the International Collegiate Baseball Conference
	query18 = Player.objects.filter(curr_team=Team.objects.filter(league=League.objects.get(name='International Collegiate Baseball Conference')))
	#...all (current) players in the American Conference of Amateur Football with last name "Lopez"
	query19 = Player.objects.filter(last_name='Lopez', curr_team=Team.objects.filter(league=League.objects.get(name='American Conference of Amateur Football')))
	#...all football players
	#...all teams with a (current) player named "Sophia"
	#...all leagues with a (current) player named "Sophia"
	#...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders

	#...all teams, past and present, that Samuel Evans has played with
	#...all players, past and present, with the Manitoba Tiger-Cats
	#...all players who were formerly (but aren't currently) with the Wichita Vikings
	#...every team that Jacob Gray played for before he joined the Oregon Colts
	#...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
	#...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
	#...all players, sorted by the number of teams they've played for
	context = {
		'atlantics': query16,
		#'penguins': query17,
		'baseball_cons': query18,
		'no_lopezes': query19,
	}
	return render(request, 'leagues/sports2.html', context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
