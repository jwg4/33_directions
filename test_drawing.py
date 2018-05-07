import unittest

from drawing import draw_line


class TestDrawLine(unittest.TestCase):
    def test_basic_line(self):
        line = [(0, 1), (1, 0.5)]
        draw_code = draw_line(line[0], line[1])
        self.assertEqual(draw_code, "\draw (0.00,1.00) -- (1.00,0.50);")