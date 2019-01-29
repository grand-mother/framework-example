# -*- coding: utf-8 -*-
"""
Unit tests for the framework_example.version module
"""

import unittest
import sys

import framework_example
from framework import git


try:
    import framework_example.version
except:
    # Skip version tests for non release builds
    pass
else:
    class VersionTest(unittest.TestCase):
        """Unit tests for the version module"""

        def test_hash(self):
            githash = git("rev-parse", "HEAD")
            self.assertEqual(githash.strip(), framework_example.version.__githash__)

        def test_version(self):
            self.assertIsNotNone(framework_example.version.__version__)


if __name__ == "__main__":
    unittest.main()
