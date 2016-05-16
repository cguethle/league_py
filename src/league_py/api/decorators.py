""" Helper decorators for LOL API calls.
"""
import functools
from league_py.api import get_region


class LolApi(object):
    """ Helper to facilitate building of the api urls for use by the basic api methods.
    """
    version = None
    name = None

    def __init__(self, url):
        self.url = url

    def __call__(self, fnc):
        @functools.wraps(fnc)
        def decorated(*args, **kwargs):
            url_pattern = "/api/lol/{region}/v{version}/{api_name}/{url_details}"

            api_url = url_pattern.format(
                region=get_region(),
                version=self.version,
                api_name=self.name,
                url_details=self.url
            )
            fnc.func_globals['api_url'] = api_url
            return fnc(*args, **kwargs)
        return decorated
