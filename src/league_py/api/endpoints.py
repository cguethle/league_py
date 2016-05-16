""" LOL endpoint servers.
"""
from league_py.regions import Regions, InvalidRegionException

_urls = {
    Regions.BRAZIL: "br.api.pvp.net",
    Regions.EUROPE_NORDIC_EAST: "eune.api.pvp.net",
    Regions.EUROPE_WEST: "euw.api.pvp.net",
    Regions.REPUBLIC_OF_KOREA: "kr.api.pvp.net",
    Regions.LATIN_AMERICA_NORTH: "lan.api.pvp.net",
    Regions.LATIN_AMERICA_SOUTH: "las.api.pvp.net",
    Regions.NORTH_AMERICA: "na.api.pvp.net",
    Regions.OCEANIA: "oce.api.pvp.net",
    Regions.TURKEY: "tr.api.pvp.net",
    Regions.RUSSIA: "ru.api.pvp.net",
    Regions.PUBLIC_BETA_ENVIRONMENT: "pbe.api.pvp.net",
    "GLOBAL": "global.api.pvp.net",
}


class NoEndpointForRegionException(Exception):
    """ Exception raised if the urls dict doesn't contain an endpoint for the supplied region name. """
    def __init__(self, region, *args, **kwargs):
        self.message = "Region '%s' does not have an endpoint configured."
        super(NoEndpointForRegionException, self).__init__(*args, **kwargs)


def get_endpoint(region):
    """
    Return the endpoint for a given region identifier.
    :param region:
    :raises: NoEndpointForRegionException
    """
    if not Regions.is_valid_region(region):
        raise InvalidRegionException(region)

    try:
        return _urls[region]
    except KeyError:
        raise NoEndpointForRegionException(region)
