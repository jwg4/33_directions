from unittest import TestCase

from geometry import planes, plane_intersection


class TestPlanes(TestCase):
    def test_length(self):
        self.assertEqual(len(planes), 6)


class TestPlaneIntersection(TestCase):
    def test_basic(self):
        vector_plane = (1, 1, 1)
        ortho_plane = (2, 2)
        intersection = plane_intersection(vector_plane, ortho_plane)
