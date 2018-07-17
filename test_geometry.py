from unittest import TestCase

from geometry import planes, plane_intersection, transform
from geometry import line_intersecting_square, get_crossing
from geometry import plane_drawing, transform_matrix


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
    
    def test_parallel(self):
        vector_plane = (1, 0, 0)
        ortho_plane = (0, 1)
        intersection = plane_intersection(vector_plane, ortho_plane)
        self.assertIsNone(intersection)


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

    def test_square_edge(self):
        plane_points = [(1, -1), (-1, 1)]
        net_points = [(1, 0), (2, 1)]
        line = (1, 0), -1
        transformed_line = transform(plane_points, net_points, line)
        coeffs, const = transformed_line
        self.assertAlmostEqual(const, 1)
        self.assertAlmostEqual(coeffs[0], 0)
        self.assertAlmostEqual(coeffs[1], 1)

    def test_squares_are_flipped(self):
        i = ((1, 0), 0)
        cube = [(1, -1), (-1, 1)]
        net = [(1, 0), (2, 1)]
        l = transform(cube, net, i, True)
        self.assertEqual(l, ((1, 0), 1.5))

    def test_diagonal_for_flipped_squares(self):
        i = ((1, 1), 0)
        cube = [(1, -1), (-1, 1)]
        net = [(1, 0), (2, 1)]
        l = transform(cube, net, i, True)
        self.assertEqual(l, ((1, -1), 1.0))


class TestTransformMatrix(TestCase):
    def test_matrix_for_flipped_squares(self):
        cube = [(1, -1), (-1, 1)]
        net = [(1, 0), (2, 1)]
        m = transform_matrix(cube, net, True)
        self.assertEqual(m, [(-2, 0), (0, 2)])


class TestLineIntersectSquare(TestCase):
    def test_intersecting_line(self):
        square = [(0, 0), (1, 1)]
        line = (1, -2), -1.5
        points = line_intersecting_square(line, square)
        self.assertEqual(points, ((0, 0.75), (0.5, 1)))

    def test_missing_line(self):
        square = [(0, 0), (1, 1)]
        line = (1, -2), 1.5
        points = line_intersecting_square(line, square)
        self.assertEqual(points, ())

    def test_edge(self):
        square = [(0, 0), (1, 1)]
        line = ((0, 1), 0.0) 
        points = line_intersecting_square(line, square)
        self.assertEqual(len(points), 2)

    def test_another_edge(self):
        net = [(0, 1), (1, 2)]
        line = ((0, 1), 2.0) 
        points = line_intersecting_square(line, net)
        self.assertEqual(len(points), 2)
        self.assertEqual(points, ((1, 2), (0, 2)))

    def test_diagonal(self):
        net = [(1, 0), (2, 1)]
        l = ((1, -1), 1.0)
        points = line_intersecting_square(l, net)
        self.assertEqual(points, ((1.0, 0.0), (2.0, 1.0)))


class TestGetCrossing(TestCase):
    def test_crossing(self):
        line = ((1, -2), -1.5)
        segment = (0, 0, [0, 1], True)
        crossing = get_crossing(line, segment)
        self.assertEqual(crossing, (0, 0.75))

    def test_missing(self):
        line = ((1, -2), -1.5)
        segment = (0, 0, [1, 2], False)
        crossing = get_crossing(line, segment)
        self.assertIsNone(crossing)

    def test_corner_to_ignore(self):
        line = ((1, 1), 1)
        segment = (0, 0, [0, 1], True)
        crossing = get_crossing(line, segment)
        self.assertIsNone(crossing)

    def test_corner_to_not_ignore(self):
        line = ((1, 1), 1)
        segment = (0, 0, [0, 1], False)
        crossing = get_crossing(line, segment)
        self.assertEqual(crossing, (0, 1))


class TestPlaneDrawing(TestCase):
    def is_almost_equal(self, x, y):
        self.assertEqual(x.__class__, y.__class__)
        if isinstance(x, list) or isinstance(x, tuple):
            return all(self.is_almost_equal(*t) for t in zip(x, y))
        return self.assertAlmostEqual(x, y)
                
    
    def test_basic_vector(self):
        v = (1, 0, 0)
        lines = plane_drawing(v)
        self.assertEqual(len(lines), 4)
        lines = set(lines)
        self.assertIn(((1.5, 0.0), (1.5, 1.0)), lines)

    def test_plane_drawing_steps(self):
        vector = (1, 0, 0)
        plane = (1, 1)
        i = plane_intersection(vector, plane)
        self.assertEqual(i, ((1, 0), 0))
        cube = [(1, -1), (-1, 1)]
        net = [(1, 0), (2, 1)]
        l = transform(cube, net, i, True)
        self.assertEqual(l, ((1, 0), 1.5))
        points = line_intersecting_square(l, net)
        self.assertEqual(points, ((1.5, 0.0), (1.5, 1.0)))
    
    def test_plane_crossing_corners(self):
        v = (1, 0, 1)
        lines = plane_drawing(v)
        self.assertEqual(len(lines), 6)
        for line in lines:
            self.assertEqual(len(line), 2)
        lines = set(lines)
        self.assertIn(((1.0, 0.0), (2.0, 1.0)), lines)
        self.assertIn(((1.0, 2.0), (0.0, 2.0)), lines)

    def test_diagonal_plane_drawing_steps(self):
        vector = (1, 0, 1)
        plane = (1, 1)
        i = plane_intersection(vector, plane)
        self.assertEqual(i, ((1, 1), 0))
        cube = [(1, -1), (-1, 1)]
        net = [(1, 0), (2, 1)]
        l = transform(cube, net, i, False)
        self.is_almost_equal(l, ((1, -1), 1.0))
        points = line_intersecting_square(l, net)
        self.is_almost_equal(points, ((1, 0.0), (2, 1.0)))

    def test_diagonal_plane_drawing_steps_second_face(self):
        vector = (1, 0, 1)
        plane = (2, 1)
        i = plane_intersection(vector, plane)
        self.assertEqual(i, ((1, 0), -1))
        cube = [(1, -1), (-1, 1)]
        net = [(0, 1), (1, 2)]
        l = transform(cube, net, i, False)
        self.assertEqual(l, ((0, 1), 2.0))
        points = line_intersecting_square(l, net)
        self.assertEqual(points, ((1.0, 2.0), (0.0, 2.0)))

    def test_diagonal_plane_drawing_steps_another_face_with_side(self):
        vector = (1, 0, 1)
        plane = (0, -1)
        i = plane_intersection(vector, plane)
        self.assertEqual(i, ((0, 1), 1))
        cube = [(1, -1), (-1, 1)]
        net = [(1, 3), (0, 2)]
        l = transform(cube, net, i, True)
        self.assertEqual(l, ((0, 1), 2.0))
        points = line_intersecting_square(l, net)
        self.assertEqual(points, ((1.0, 2.0), (0.0, 2.0)))
