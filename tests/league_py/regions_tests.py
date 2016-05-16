""" Tests for regions module.
"""
from unittest import TestCase

from league_py.regions import Regions


class BasicUseCases(TestCase):

    def test_is_valid_region(self):
        """ Validate Regions.is_valid_region utility method.
        """
        self.assertTrue(Regions.is_valid_region(Regions.BRAZIL),
                        "%s should be considered a valid region." % Regions.BRAZIL)

        self.assertFalse(Regions.is_valid_region("not valid region"),
                         "is_valid_region passed, but should have failed.")
