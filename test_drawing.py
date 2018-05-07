import unittest

from drawing import draw_line


class TestDrawLine(unittest.TestCase):
    def test_basic_line(self):
        x = (0, 1)
        z = (1, 0.5)
        draw_code = draw_line(x, z)
        self.assertEqual(draw_code, "    \draw (0.00,1.00) -- (1.00,0.50);")
        
    def test_basic_line_with_star(self):
        line = [(0, 1), (1, 0.5)]
        draw_code = draw_line(*line)
        self.assertEqual(draw_code, "    \draw (0.00,1.00) -- (1.00,0.50);")