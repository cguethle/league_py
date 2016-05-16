""" Tests for summoner API
"""
from unittest import TestCase
from league_py.api import set_region, set_api_key
from league_py.regions import Regions

from league_py.api.summoner import get_summoners_by_name


class SummonerApiUseCases(TestCase):
    api_key = "your_api_key"

    def test_get_summoners_by_name(self):

        set_region(Regions.BRAZIL)
        set_api_key(self.api_key)

        summoners = ['1', '2']

        summoners_by_name = get_summoners_by_name(summoners)

        print summoners_by_name

        self.fail()
