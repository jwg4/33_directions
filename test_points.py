from unittest import TestCase

from points import generate_points


class TestGeneratePoints(TestCase):
    def test_number_of_points(self):
        points = list(generate_points())
        self.assertEqual(33, len(points))
