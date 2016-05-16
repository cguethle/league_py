from league_py.api import game as game_api
from league_py.dto.raw_stats import get_raw_stats_manager
from league_py.dto.player import get_player_manager

game_manager = None


class GameManager(object):

    def get_recent_games(self, summoner_id):
        """
        Returns recents games played.
        :param summoner_id: Summoner Id
        :return: List of games
        :rtype: list of Game
        """
        games_json = game_api.get_games(summoner_id)
        games = [self.from_json(game_dict) for game_dict in games_json['games']]

        return games

    @staticmethod
    def from_json(json_payload):
        """
        Generate a Game object from the Lol Api Json.
        :param json_payload: Lol Api Json Payload.
        :return: Game object
        :rtype: Game
        """
        player_manager = get_player_manager()

        g = Game()
        g.game_id = json_payload['gameId']
        g.champion_id = json_payload['championId']
        g.level = json_payload['level']
        g.stats = get_raw_stats_manager().from_json(json_payload['stats'])
        g.fellow_players = [player_manager.from_json(player_payload)
                            for player_payload in json_payload['fellowPlayers']]
        return g


def get_game_manager():
    global game_manager
    if game_manager is None:
        game_manager = GameManager()
    return game_manager


class Game(object):
    champion_id = None
    create_date = None
    fellow_players = None
    game_id = None
    game_mode = None
    game_type = None
    invalid = None
    ip_earned = None
    level = None
    map_id = None
    spell1 = None
    spell2 = None
    stats = None            # type: RawStats
    subtype = None
    team_id = None

    # cached objects
    _champion = None        # type: Champion
    _team = None            # type: Team

    @property
    def champion(self):
        """ Helper to lazy load champion object based on champion_id.
        :rtype: Champion
        """
        return self._champion

    @property
    def team(self):
        """ Helper to lazy load team object based on team_id.
        :rtype: Team
        """
        return self._team
