from league_py.api.summoner import get_summoners_by_name
from league_py.api import set_region, set_api_key
from league_py.regions import Regions
set_region(Regions.NORTH_AMERICA)
from django.conf import settings
set_api_key(settings.LOL_API_KEY)
for x in range(11):
    get_summoners_by_name('Tourmalyn')