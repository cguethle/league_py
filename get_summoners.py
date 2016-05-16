import json, csv

from league_py.api import set_api_key, set_region
from league_py.regions import Regions
from league_py.dto.summoner import get_summoner_manager

set_region(Regions.NORTH_AMERICA)
set_api_key('your_api_key')

my_summoner = get_summoner_manager().get_by_name('Tourmalyn')
number_of_recent_games = len(my_summoner.recent_games)


print my_summoner.name

print "Average Damage: %s" % (sum(game.stats.total_damage_dealt_to_champions
                                  for game in my_summoner.recent_games) / number_of_recent_games)

print "Average Physical Damage: %s" % (sum(game.stats.physical_damage_dealt_to_champions
                                           for game in my_summoner.recent_games) / number_of_recent_games)

print "Average Magic Damage: %s" % (sum(game.stats.magic_damage_dealt_to_champions
                                        for game in my_summoner.recent_games) / number_of_recent_games)
