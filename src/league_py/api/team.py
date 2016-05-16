""" Methods and such for accessing the team api.
"""
import requests

from league_py.api.decorators import LolApi
from league_py.api import get_url


class TeamApi(LolApi):
    """ Decorator for TeamApis """
    version = "2.4"
    name = "team"


@TeamApi(url="by-summoner/{summoner_ids}")
def get_teams_by_summoner_ids(ids):
    """ Lookup information on a teams using summoner ids.
    :param ids: Ids of summoners on teams to lookup.
    :type ids: list or str
    :return:
    """
    ids = ids if isinstance(ids, list) else [ids]
    resp = requests.get(get_url(api_url, summoner_ids=','.join(str(i) for i in ids)))

    return resp.json()


@TeamApi(url="{team_ids}")
def get_teams(ids):
    """ Lookup information on a teams using summoner ids.
    :param ids: Ids of summoners on teams to lookup.
    :type ids: list or str
    :return:
    """
    ids = ids if isinstance(ids, list) else [ids]
    resp = requests.get(get_url(api_url, team_ids=','.join(str(i) for i in ids)))

    return resp.json()
