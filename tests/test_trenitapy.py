#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_trenitapy
----------------------------------

Tests for `trenitapy` module.
"""

import unittest
from datetime import date, datetime, time, timedelta

from trenitapy.trenitapy import TrenitApy


class TestTrenitapy(unittest.TestCase):

    def setUp(self):
        self.api = TrenitApy()

    def tearDown(self):
        pass

    def test_andamento_treno(self):
        assert isinstance(self.api.andamento_treno('S00228', '4640'), dict)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
