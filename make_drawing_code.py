# coding=utf-8
import math
import random

from drawing import draw_line, draw_point
from geometry import plane_drawing, antipodes
from points import color_points


def drawing_code(points):
    for p, color in points:
        if p[0] in [1, -1]:
            for line in plane_drawing(p):
                c = draw_line(*line, color=color)
                yield c
        for point in antipodes(p):
            c = draw_point(point, color=color)
            yield c


if __name__ == '__main__':
    s = "\n".join(drawing_code(color_points()))
    with open("planes.tex", "w") as f:
        f.write(s)
