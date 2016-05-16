""" Methods and such for accessing the champion api.
"""
import requests

from league_py.api.decorators import LolApi
from league_py.api import get_url


class ChampionApi(LolApi):
    """ Decorator for TeamApis """
    version = "1.2"
    name = "champion"


@ChampionApi(url="")
def get_champions():
    """ Lookup information on all champions.
    :return:
    """
    resp = requests.get(get_url(api_url))

    return resp.json()


@ChampionApi(url="{champion_id}")
def get_champion(champion_id):
    """ Lookup information on all champions.
    :param champion_id: Id of the champion to pull info for.
    :return:
    """
    resp = requests.get(get_url(api_url, champion_id=champion_id))

    return resp.json()
