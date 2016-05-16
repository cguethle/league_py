from league_py.api import summoner as summoner_api
from league_py.dto.game import get_game_manager
from pytz import utc
from datetime import datetime

__all__ = ['get_summoner_manager', 'Summoner']

summoner_manager = None


class SummonerManager(object):

    @staticmethod
    def get_by_name(summoner_name):
        """
        :type summoner_name: str
        :return:
        :rtype: league_py.dto.summoner.Summoner
        """
        summoner_id = summoner_api.get_summoners_by_name(summoner_name)[summoner_name.lower()]['id']
        return Summoner(summoner_id)


def get_summoner_manager():
    global summoner_manager
    if summoner_manager is None:
        summoner_manager = SummonerManager()
    return summoner_manager


class Summoner(object):

    id = None
    name = None
    level = None
    profile_icon_id = None
    revision_date = None
    recent_games = None

    def __init__(self, summoner_id):
        """
        Load summoner by id.
        :param summoner_id: Id of the summoner.
        :return:
        """
        summoner_details = summoner_api.get_summoners(summoner_id)[str(summoner_id)]

        self.id = summoner_details['id']
        self.name = summoner_details['name']
        self.level = summoner_details['summonerLevel']
        self.profile_icon_id = summoner_details['profileIconId']
        self.revision_date = utc.localize(datetime.utcfromtimestamp(summoner_details['revisionDate'] / 1000))
        self.recent_games = get_game_manager().get_recent_games(summoner_id)

