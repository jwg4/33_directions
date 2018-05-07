from unittest import TestCase

from geometry import planes, plane_intersection, transform
from geometry import line_intersecting_square, get_crossing
from geometry import plane_drawing


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
        self.assertAlmostEqual(const, -2)
        self.assertAlmostEqual(coeffs[0], 1)
        self.assertAlmostEqual(coeffs[1], -1)


class TestLineIntersectSquare(TestCase):
    def test_intersecting_line(self):
        square = [(0, 0), (1, 1)]
        line = (1, -2), -1.5
        points = line_intersecting_square(line, square)
        self.assertEqual(points, [(0, 0.75), (0.5, 1)])

    def test_missing_line(self):
        square = [(0, 0), (1, 1)]
        line = (1, -2), 1.5
        points = line_intersecting_square(line, square)
        self.assertEqual(points, [])


class TestGetCrossing(TestCase):
    def test_crossing(self):
        line = ((1, -2), -1.5)
        segment = (0, 0, [0, 1])
        crossing = get_crossing(line, segment)
        self.assertEqual(crossing, (0, 0.75))

    def test_missing(self):
        line = ((1, -2), -1.5)
        segment = (0, 0, [1, 2])
        crossing = get_crossing(line, segment)
        self.assertIsNone(crossing)


class TestPlaneDrawing(TestCase):
    def test_basic_vector(self):
        v = (1, 0, 0)
        lines = plane_drawing(v)
        self.assertEqual(len(lines), 4)
