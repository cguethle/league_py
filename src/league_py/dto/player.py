player_manager = None


class PlayerManager(object):

    @staticmethod
    def from_json(json_payload):
        p = Player()
        p.champion_id = json_payload['championId']
        p.summoner_id = json_payload['summonerId']
        p.team_id = json_payload['teamId']
        return p


def get_player_manager():
    global player_manager
    if player_manager is None:
        player_manager = PlayerManager()
    return player_manager


class Player(object):
    champion_id = None
    summoner_id = None
    team_id = None

    # cached objects
    _champion = None
    _summoner = None
    _team = None

    @property
    def champion(self):
        return self._champion

    @property
    def summoner(self):
        return self._summoner

    @property
    def team(self):
        return self._team
