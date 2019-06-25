from unittest import TestCase

import coord


class TestCoord(TestCase):

    def setUp(self):
        """Init"""

    def test_count_position(self):

        self.assertEqual(coord.count_position('LU'), (-1, 1))
        self.assertEqual(coord.count_position('UU'), (0, 2))

    def test_conclusion(self):

        self.assertTrue(coord.conclusion('UD'))

    def tearDown(self):
        """Finish"""
