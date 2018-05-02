from unittest import TestCase

from geometry import planes


class TestPlanes(TestCase):
    def test_length(self):
        self.assertEqual(len(planes), 6)