import copy
import tempfile
import unittest

import tests.runner as runner
from edgescan.constants import ASSETS, HOSTS, LICENSES, VULNERABILITIES
from tests.client import client


class CLITestCases(unittest.TestCase):
    api = copy.copy(client)

    def test_cli(self):
        for resource_type in (ASSETS, HOSTS, LICENSES, VULNERABILITIES):
            with self.subTest(resource_type=resource_type):
                self._test_cli(resource_type)

    def _test_cli(self, resource_type: str):
        rows = self.api.iter_objects(resource_type=resource_type)
        row = next(rows, None)
        if row is None:
            raise unittest.SkipTest(f"No {resource_type} found")

        with tempfile.NamedTemporaryFile() as file:
            temporary_file = file.name

            commands = [
                ["get", resource_type, row["id"]],
                ["list", resource_type],
                ["list", resource_type, "--id", row["id"]],
                ["count", resource_type],
                ["count", resource_type, "--id", row["id"]],
                ["export", resource_type, temporary_file],
            ]
            for args in commands:
                with self.subTest(args=args):
                    result = runner.invoke(*args)
                    command = " ".join(map(str, args))
                    with self.subTest(command=command):
                        self.assertEqual(0, result.exit_code)
