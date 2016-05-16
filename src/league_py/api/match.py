""" Methods and such for accessing the match api.
"""
import requests

from league_py.api.decorators import LolApi
from league_py.api import get_url


class MatchApi(LolApi):
    """ Decorator for TeamApis """
    version = "2.2"
    name = "match"


@MatchApi(url="{match_id}")
def get_match(id):
    """ Lookup information on a teams using summoner ids.
    :param ids: Ids of summoners on teams to lookup.
    :type ids: list or str
    :return:
    """
    resp = requests.get(get_url(api_url, match_id=id))

    return resp.json()
