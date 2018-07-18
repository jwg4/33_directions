import unittest

from drawing import draw_line, draw_point


class TestDrawLine(unittest.TestCase):
    def test_basic_line(self):
        x = (0, 1)
        z = (1, 0.5)
        draw_code = draw_line(x, z)
        self.assertEqual(draw_code, "    \draw[black] (0.00,1.00) -- (1.00,0.50);")
        
    def test_basic_line_with_star(self):
        line = [(0, 1), (1, 0.5)]
        draw_code = draw_line(*line, color="red")
        self.assertEqual(draw_code, "    \draw[red] (0.00,1.00) -- (1.00,0.50);")


class TestDrawPoint(unittest.TestCase):
    def test_basic_point(self):
        p = (0.5, 2.5)
        draw_code = draw_point(p, "green")
        expected = "    \draw[green] (0.50,2.50) circle (1pt);"
        self.assertEqual(expected, draw_code)
