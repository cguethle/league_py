""" Methods and such for accessing the league api.
"""
import requests

from league_py.api.decorators import LolApi
from league_py.api import get_url


class LeagueApi(LolApi):
    """ Decorator for TeamApis """
    version = "2.5"
    name = "league"


@LeagueApi(url="by-summoner/{summoner_ids}")
def get_leagues_by_summoner(summoner_ids):
    """ Lookup information on leagues by using summoner ids.
    :param summoner_ids: Ids of the summoners to lookup.
    :return:
    """
    resp = requests.get(get_url(api_url, summoner_ids=summoner_ids))

    return resp.json()


@LeagueApi(url="by-summoner/{summoner_ids}/entry")
def get_league_entries_by_summoner(summoner_ids):
    """ Lookup information on league entries by using summoner ids.
    :param summoner_ids: Ids of the summoners to lookup.
    :return:
    """
    resp = requests.get(get_url(api_url, summoner_ids=summoner_ids))

    return resp.json()


@LeagueApi(url="by-team/{team_ids}")
def get_leagues_by_team(team_ids):
    """ Lookup information on leagues by using team ids.
    :param summoner_ids: Ids of the teams to lookup.
    :return:
    """
    resp = requests.get(get_url(api_url, team_ids=team_ids))

    return resp.json()


@LeagueApi(url="by-summoner/{team_ids}/entry")
def get_league_entries_by_team(team_ids):
    """ Lookup information on league entries by using team ids.
    :param summoner_ids: Ids of the teams to lookup.
    :return:
    """
    resp = requests.get(get_url(api_url, team_ids=team_ids))

    return resp.json()


@LeagueApi(url="challenger")
def get_challenger_leagues():
    """ Get challenger tier leagues.
    :return:
    """
    resp = requests.get(get_url(api_url))

    return resp.json()


@LeagueApi(url="master")
def get_master_leagues():
    """ Get master tier leagues.
    :return:
    """
    resp = requests.get(get_url(api_url))

    return resp.json()
