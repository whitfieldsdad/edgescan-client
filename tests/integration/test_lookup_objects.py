import copy
import tempfile
import unittest
from unittest import TestCase

from edgescan.constants import ASSETS, HOSTS, LICENSES, VULNERABILITIES
from tests.client import client


class IntegrationTests(TestCase):
    api = copy.copy(client)

    def test_get_resources(self):
        for resource_type in (ASSETS, HOSTS, LICENSES, VULNERABILITIES):
            with self.subTest(resource_type=resource_type):
                rows = tuple(self.api.iter_objects(resource_type=resource_type))
                if not any(rows):
                    raise unittest.SkipTest(f"No {resource_type} found")

                self.assertTrue(all(isinstance(row, dict) for row in rows))

    def test_count_resources(self):
        for resource_type in (ASSETS, HOSTS, LICENSES, VULNERABILITIES):
            with self.subTest(resource_type=resource_type):
                total = self.api.count_objects(resource_type=resource_type)
                self.assertTrue(isinstance(total, int))

    def test_export_resources(self):
        for resource_type in (ASSETS, HOSTS, LICENSES, VULNERABILITIES):
            with self.subTest(resource_type=resource_type):
                total = self.api.count_objects(resource_type=resource_type)
                if total == 0:
                    raise unittest.SkipTest(f"No {resource_type} found")

                with tempfile.NamedTemporaryFile() as file:
                    path = file.name
                    self.api.export_objects(resource_type=resource_type, path=path)
