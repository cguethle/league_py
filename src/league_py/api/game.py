""" Methods and such for accessing the game api.
"""
import requests

from league_py.api.decorators import LolApi
from league_py.api import get_url


class GameApi(LolApi):
    """ Decorator for MatchListApi """
    version = "1.3"
    name = "game"


@GameApi(url="by-summoner/{summoner_id}/recent")
def get_games(id):
    """ Lookup information on a teams using summoner ids.
    :param ids: Ids of summoners on teams to lookup.
    :type ids: list or str
    :return:
    """
    resp = requests.get(get_url(api_url, summoner_id=id))

    return resp.json()
