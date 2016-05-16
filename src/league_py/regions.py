""" Region Constants
"""


class Regions(object):
    BRAZIL = "br"
    EUROPE_NORDIC_EAST = "eune"
    EUROPE_WEST = "euw"
    LATIN_AMERICA_NORTH = "lan"
    LATIN_AMERICA_SOUTH = "las"
    NORTH_AMERICA = "na"
    OCEANIA = "oce"
    RUSSIA = "ru"
    TURKEY = "tr"
    SOUTH_EAST_ASIA = "sea"
    REPUBLIC_OF_KOREA = "kr"
    PUBLIC_BETA_ENVIRONMENT = "pbe"

    _regions_list = [BRAZIL, EUROPE_NORDIC_EAST, EUROPE_WEST, LATIN_AMERICA_NORTH, LATIN_AMERICA_SOUTH, NORTH_AMERICA,
                     OCEANIA, RUSSIA, TURKEY, SOUTH_EAST_ASIA, REPUBLIC_OF_KOREA, PUBLIC_BETA_ENVIRONMENT]

    @classmethod
    def is_valid_region(cls, region):
        """
        Returns whether this is a valid region or not.
        :param region: Name of the region.
        :type region: str
        :return: True|False based on the validity of the region.
        :rtype: bool
        """
        return region in cls._regions_list


class InvalidRegionException(ValueError):
    """ Exception raised if set_region is called with an invalid region.  See league_py.regions for valid values. """
    def __init__(self, region, *args, **kwargs):
        self.message = "Region '%s' is not a valid region.  See league_py.regions for valid values."
        super(InvalidRegionException, self).__init__(*args, **kwargs)
