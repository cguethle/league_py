""" Tests for basic utils in api module
"""
from unittest import TestCase
from datetime import datetime, timedelta
from collections import deque

from league_py.api import InvalidRegionException, NoRegionSelectedException
from league_py.api import set_region, get_region, set_api_key, get_api_key
from league_py.api.base import Throttle, ThrottledException
from league_py.regions import Regions
from freezegun import freeze_time


class BasicUseCases(TestCase):

    def setUp(self):
        # cleared cached values for each test.
        set_region()
        set_api_key()

    def test_set_region(self):
        """ Test league_py.api.set_region with a good/bad region string.
        """
        # no return, but should not throw exception.
        set_region(Regions.BRAZIL)

        with self.assertRaises(InvalidRegionException):
            set_region('invalid region')

    def test_get_region(self):
        """ Test league_py.api.get_region
        """
        with self.assertRaises(NoRegionSelectedException):
            get_region()

        expected_region = Regions.BRAZIL

        set_region(expected_region)

        self.assertEqual(get_region(), expected_region)

    def test_setget_api_key(self):
        """ Test league_py.api.set_api_key
        """
        api_key = "123abc"
        set_api_key(api_key)

        self.assertEqual(get_api_key(), api_key)


class ThrottleTestCases(TestCase):
    """ Test Throttle
    """

    def test_decay(self):
        """ Validate _decay private method.
        :return:
        """
        throttle = Throttle(seconds=1, count=4)

        now = datetime.now()
        request_times = [
            now, now + timedelta(seconds=1), now + timedelta(seconds=2), now + timedelta(seconds=3)
        ]

        test_cases = [
            (now, 4),
            (now + timedelta(minutes=1), 0),
            (now + timedelta(seconds=2, milliseconds=1), 2)
        ]

        for time_to_freeze, expected_remaining in test_cases:
            throttle._request_times = deque(request_times, maxlen=4)
            with freeze_time(time_to_freeze):
                throttle._decay()
                self.assertEqual(len(throttle._request_times), expected_remaining)

    def test_request_slot(self):
        """ Validate request_slot method on Throttle object.
        :return:
        """
        throttle = Throttle(seconds=1, count=4)

        now = datetime.now()

        with freeze_time(now):
            for x in range(4):
                accepted, _ = throttle.request_slot()
                self.assertTrue(accepted)

            accepted, next_time = throttle.request_slot()
            self.assertFalse(accepted)
            self.assertEqual(next_time, now + timedelta(seconds=1, milliseconds=1))

        self.fail('This test is not complete yet...')
