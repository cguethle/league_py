from datetime import datetime, timedelta
import requests
from gevent import Greenlet
from collections import deque
from logging import getLogger

LOG = getLogger()
RATE_LIMIT_STATUS_CODE = 429

__all__ = ['riot_api']


class RateLimitedException(Exception):
    message = "Api is Ratelimited.  Backoff!"


class ThrottledException(Exception):
    message = "Queue is full."


class Throttle(object):
    """
    This Throttle object is NOT intended for high volume or distributed use.  It gets the job done for a small project,
    but not much beyond that...  Use with care.
    """

    _seconds = None
    _count = None
    _free = None
    _request_times = None

    def __init__(self, seconds, count):
        self._seconds = timedelta(seconds=seconds)
        self._count = count
        self._last_check = datetime.now()
        self._free = count
        self._request_times = deque([], maxlen=count)

    def request_slot(self):
        """ Check to see if we are exhausted.
        :return: A tuple indicating if the request was approved, and if not, the next time available where a request
        might be accepted. Note that depending on volume of calls to request_slot, the 'next time available' is not
        guaranteed, and should not be looked on as a reservation, but instead a time to try again.

        TODO: enable a reservation concept when requests are rejected.
        """
        if len(self._request_times) > 0:
            LOG.debug("_request_times is not empty, decaying.")
            self._decay()

        if len(self._request_times) < self._count:
            now = datetime.now()
            LOG.debug("There is room in _request_times, allow request and log entry %s.", now)
            self._request_times.append(now)

            return True, None
        else:
            # next available is the oldest one, plus the time period, plus a 1 millisecond buffer.
            LOG.debug("Throttled!!!!")
            LOG.debug(" - ".join(map(str, [self._request_times[0], self._seconds, timedelta(milliseconds=1)])))
            next_available = self._request_times[0] + self._seconds + timedelta(milliseconds=1)
            LOG.debug("_request_times is full.  Next available ~ %s", next_available)
            return False, next_available

    def _decay(self):
        """
        Decay the request times queue.
        :return:
        """
        boundary = datetime.now() - self._seconds  # boundary where items are too old to care about.
        LOG.debug("boundary is %s", boundary)
        try:
            while self._request_times[0] < boundary:
                # Remove entries that are too old (not impacting the throttle counts)
                LOG.debug("%s is too old, popping from _request_times.", self._request_times[0])
                self._request_times.popleft()
        except IndexError:
            LOG.debug("request times deque is empty.  All old entries flushed.")


class RiotApi(object):

    _throttles = []

    _allowance = None

    _executions_last_ten_sec = 0
    _executions_last_ten_min = 0

    _rate_limited = False
    _call_count = []   # rolling list of call counts per sec.

    def __init__(self, *rates):
        for num_seconds, count in rates:
            self._throttles.append(Throttle(num_seconds, count))

    def call(self, url):
        """
        Attempt to call the riotapi.
        :param url:
        :return:
        """
        if True:
            return self._call_api(url)

        current = datetime.now()
        time_passed = current - self._allowed_rates[10]["last_check"]

        g = Greenlet(self._call_api, url=url)

        execute_now, seconds_till_execution = self._queue_api_call()
        if execute_now:
            g.start()
            return g.get()
        else:
            g.start_later(seconds_till_execution).get()
            return g.get()

    def _queue_api_call(self):
        """
        Queue up an api call.  If it can be called immediately, return indicating that.
        :return:
        """
        if self._api_calls_available():
            return True, None

    def _update_counts(self):
        """
        Update the
        :return:
        """


    def _call_api(self, url):
        """
        Actually call api.
        :param url:
        :return:
        """
        resp = requests.get(url)

        if resp.status_code == RATE_LIMIT_STATUS_CODE:
            self._rate_limited = True
            raise RateLimitedException()

        return resp

    def _api_calls_available(self):
        return \
            self._executions_last_ten_sec < self._rate_per_ten_sec and \
            self._executions_last_ten_min < self._rate_per_ten_min

riot_api = RiotApi()
