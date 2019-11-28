# -*-coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
from django.test import TestCase


class SimpleTest(TestCase):

    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)
