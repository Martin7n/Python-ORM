import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Match, Tournament
from main_app import models
from django.db.models import Count, Q

# Create queries within functions

# a = TennisPlayer.objects.filter(id=1)
# for player in a:
#     print(player.matches__set)
# b = TennisPlayer.objects.all()
# res = []
# for player in b:
#     a = Match.objects.filter(winner=player).values_list('score', 'winner')
#     print(a)
#     res.append(a)
# for match in a:
#
#     print(match.summary, match.winner)

# for x in res:
#     print(x)


#
# for player in b:
#
# a = TennisPlayer.objects.get_tennis_players_by_wins_count()
# print(a)



def get_tennis_players(search_name=None, search_country=None):
    result = []
    if search_name is None and search_country is None:
        return ""
    elif search_name is None and search_country is not None:
        players =  TennisPlayer.objects.filter(country__icontains=search_country).order_by('ranking')
        result.append(x for x in players)
    elif search_name is not None and search_country is None:
        players =  TennisPlayer.objects.filter(full_name__icontains=search_name).order_by('ranking')
        result.append(x for x in players)
    elif search_country is not None and search_name is not None:
        query = Q(full_name__icontains=search_name) & Q(country__icontains=search_country)
        players =  TennisPlayer.objects.filter(query).order_by('ranking')
        result.append(x for x in players)

    if len(result) < 1:
        return ""
    return "\n".join(f'Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}' for player  in players)

# print(get_tennis_players(None,'Serbia'))


def get_top_tennis_player():
    a = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    if a:
        return f"Top Tennis Player: {a.full_name} with {a.wins_count} wins."
    return ""


# print(get_top_tennis_player())

def get_tennis_player_by_matches_count():
    b = TennisPlayer.objects.annotate(matches_count=Count('matches')).order_by('-matches_count', 'ranking').first()
    if b and b.matches_count>0:
        return f"Tennis Player: {b.full_name} with {b.matches_count} matches played."
    return ""


def get_tournaments_by_surface_type(surface=None):
    results = []
    if surface is None:
        return ''
    query = Q(surface_type__icontains=surface)
    tournaments = Tournament.objects.filter(query).annotate(surface_matches=Count(query), match_count=(Count('matches'))).order_by('-start_date')
    if not tournaments:
        return ''

    return "\n".join(f'Tournament: {x.name}, start date: {x.start_date}, matches: {x.match_count}' for x in tournaments)


print(get_tournaments_by_surface_type("z"))


def get_latest_match_info():

    latest_match = Match.objects \
        .prefetch_related('players') \
        .order_by('-date_played', '-id') \
        .first()

    if latest_match is None:
        return ""
    players = latest_match.players.order_by('full_name')
    player1_full_name = players.first().full_name
    player2_full_name = players.last().full_name
    winner_full_name = "TBA" if latest_match.winner is None else latest_match.winner.full_name

    return f"Latest match played on: {latest_match.date_played}, tournament: {latest_match.tournament.name}, " \
           f"score: {latest_match.score}, players: {player1_full_name} vs {player2_full_name}, " \
           f"winner: {winner_full_name}, summary: {latest_match.summary}"

# print(get_latest_match_info())

def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    matches = Match.objects.select_related('tournament', 'winner').filter(tournament__name__exact=tournament_name).order_by('-date_played')

    if not matches:
        return "No matches found."
    # for match in matches:
    #     print(match.winner)
    return '\n'.join(f"Match played on: {x.date_played}, score: {x.score}, winner: {x.winner.full_name if x.winner else 'TBA'}" for x in matches)


print(get_matches_by_tournament("Boo"))