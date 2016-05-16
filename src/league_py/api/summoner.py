""" Methods and such for accessing the summoner api.
"""
import requests

from league_py.api.decorators import LolApi
from league_py.api import get_url
from league_py.api.base import riot_api


class SummonerApi(LolApi):
    """ Decorator for SummonerApis """
    version = "1.4"
    name = "summoner"


@SummonerApi(url="by-name/{summoner_names}")
def get_summoners_by_name(names):
    """ Lookup information on a list of summoners using the following API.

    /api/lol/<region>/v<version>/summoner/by-name/

    :param name: Names of the summoners to lookup.
    :type name: list
    :return:
    """
    names = names if isinstance(names, list) else [names]
    resp = riot_api.call(get_url(api_url, summoner_names=','.join(names)))

    return resp.json()


@SummonerApi(url="by-account/{account_ids}")
def get_summoners_by_account_id(ids):
    """ Lookup information on a list of summoners using the following API.

    /api/lol/<region>/v<version>/summoner/by-name/

    :param name: Names of the summoners to lookup.
    :type name: list
    :return:
    """
    ids = ids if isinstance(ids, list) else [ids]
    resp = requests.get(get_url(api_url, account_ids=','.join(str(i) for i in ids)))

    return resp.json()


@SummonerApi(url="{summoner_ids}")
def get_summoners(ids):
    """ Lookup information on a list of summoners using the following API.
    :param name: Names of the summoners to lookup.
    :type name: list
    :return:
    """

    ids = ids if isinstance(ids, list) else [ids]
    resp = requests.get(get_url(api_url, summoner_ids=','.join(str(i) for i in ids)))

    return resp.json()


@SummonerApi(url="{summoner_ids}/masteries")
def get_summoners_masteries(ids):
    """ Lookup mastery information for a list of summoners.
    :param ids: Summoner Ids of the summoners to lookup.
    :type ids: list
    :return:
    """
    ids = ids if isinstance(ids, list) else [ids]
    resp = requests.get(get_url(api_url, summoner_ids=','.join(str(i) for i in ids)))

    return resp.json()


@SummonerApi(url="{summoner_ids}/name")
def get_summoners_name(ids):
    """ Lookup name information for a list of summoners.
    :param ids: Summoner Ids of the summoners to lookup.
    :type ids: list
    :return:
    """
    ids = ids if isinstance(ids, list) else [ids]
    resp = requests.get(get_url(api_url, summoner_ids=','.join(str(i) for i in ids)))

    return resp.json()


@SummonerApi(url="{summoner_ids}/runes")
def get_summoners_runes(ids):
    """ Lookup rune information for a list of summoners.
    :param ids: Summoner Ids of the summoners to lookup.
    :type ids: list
    :return:
    """
    ids = ids if isinstance(ids, list) else [ids]
    resp = requests.get(get_url(api_url, summoner_ids=','.join(str(i) for i in ids)))

    return resp.json()
