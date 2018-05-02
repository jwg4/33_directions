from unittest import TestCase

from geometry import planes, plane_intersection, transform


class TestPlanes(TestCase):
    def test_length(self):
        self.assertEqual(len(planes), 6)


class TestPlaneIntersection(TestCase):
    def test_basic(self):
        vector_plane = (1, 1, 1)
        ortho_plane = (2, 2)
        intersection = plane_intersection(vector_plane, ortho_plane)
        coeffs, const = intersection
        self.assertEqual(coeffs, (1, 1))
        self.assertEqual(const, -2)


class TestTransform(TestCase):
    def test_project_to_net(self):
        plane_points = [(1, -1), (-1, 1)]
        net_points = [(0, 1), (1, 2)]
        line = (1, 1), -2
        transformed_line = transform(plane_points, net_points, line)
        coeffs, const = transformed_line
        self.assertEqual(const, 0)
        self.assertEqual(coeffs, (-2, 2))
    