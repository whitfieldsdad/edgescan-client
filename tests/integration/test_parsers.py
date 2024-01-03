import copy
import functools
import unittest
from unittest import TestCase

import edgescan.data.parser
from edgescan import Asset, Host, License, Vulnerability
from edgescan.constants import ASSETS, HOSTS, LICENSES, VULNERABILITIES
from tests.client import client


class ParserTestCases(TestCase):
    api = copy.copy(client)
    maxDiff = None

    def test_parsers(self):
        for resource_type, expected_return_type in (
            (ASSETS, Asset),
            (HOSTS, Host),
            (LICENSES, License),
            (VULNERABILITIES, Vulnerability),
        ):
            with self.subTest(resource_type=resource_type):
                rows = tuple(self.api.iter_objects(resource_type=resource_type))
                if not any(rows):
                    raise unittest.SkipTest(f"No {resource_type} found")

                parser = functools.partial(
                    edgescan.data.parser.parse_object, resource_type=resource_type
                )
                for row in rows:
                    obj = parser(row)
                    self.assertIsInstance(obj, expected_return_type)
