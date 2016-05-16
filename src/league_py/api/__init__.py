""" Base API utilities.
"""
from league_py.regions import Regions, InvalidRegionException
from league_py.api.endpoints import get_endpoint

BASE_LOL_API_URL = "/api/lol/{region}/v{version}"

CACHED_REGION = None
CACHED_API_KEY = None


class NoRegionSelectedException(Exception):
    """ Exception raised if no region is cached.
    """
    def __init__(self, *args, **kwargs):
        self.message = "No region is selected/cached.  Call league_py.api.set_region with an appropriate value."
        super(NoRegionSelectedException, self).__init__(*args, **kwargs)


class ApiKeyNotSetException(Exception):
    """ Exception raised if no region is cached.
    """
    def __init__(self, *args, **kwargs):
        self.message = "No api key is selected/cached.  Call league_py.api.set_api_key with an appropriate value."
        super(ApiKeyNotSetException, self).__init__(*args, **kwargs)


def set_region(region=None):
    """
    Cache the region you want to use for api requests.
    :param region: The region to use for api requests.  This should be one of league_py.regions.  This is optional, and
    if not provided, the region cache will be cleared.
    :type region: str
    :raises: InvalidRegionException
    """
    if region and not Regions.is_valid_region(region):
        raise InvalidRegionException(region)

    global CACHED_REGION
    CACHED_REGION = region


def get_region():
    """
    Returns the cached region, or raises exception.
    :raises: NoRegionSelectedException
    """
    if CACHED_REGION is None:
        raise NoRegionSelectedException()

    return CACHED_REGION


def set_api_key(api_key=None):
    """
    Cache the api key for use in requests.
    :param api_key: Value of your api key.  This is optional, and if not provided, the api key cache will be cleared.
    :type api_key: str
    """
    global CACHED_API_KEY
    CACHED_API_KEY = api_key


def get_api_key():
    """
    Get the API key from cache.
    :return: Api key
    :rtype: str
    """
    if CACHED_API_KEY is None:
        raise ApiKeyNotSetException()

    return CACHED_API_KEY


def get_url(url_pattern, **pattern_args):
    """
    Get a final api url based on the incoming pattern and kwargs.
    :param url_pattern:
    :return:
    """
    url = ''.join([
        "https://",
        get_endpoint(get_region()),
        url_pattern.format(**pattern_args),
        "?api_key=",
        get_api_key()
    ])

    return url
