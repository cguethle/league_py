""" Methods and such for accessing the matchlist api.
"""
import requests

from league_py.api.decorators import LolApi
from league_py.api import get_url


class MatchListApi(LolApi):
    """ Decorator for MatchListApi """
    version = "2.2"
    name = "matchlist"


@MatchListApi(url="by-summoner/{summoner_id}")
def get_matchlist(id):
    """ Lookup information on a teams using summoner ids.
    :param ids: Ids of summoners on teams to lookup.
    :type ids: list or str
    :return:
    """
    resp = requests.get(get_url(api_url, summoner_id=id))

    return resp.json()
