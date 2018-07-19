# coding=utf-8
import math
import random
import sys

from drawing import draw_line, draw_point
from geometry import plane_drawing, antipodes
from points import color_points


def drawing_code(points, sparse=False):
    for p, color in points:
        if (not sparse) or p[0] in [1, -1]:
            for line in plane_drawing(p):
                c = draw_line(*line, color=color)
                yield c
        for point in antipodes(p):
            c = draw_point(point, color=color)
            yield c


if __name__ == '__main__':
    sparse = "--sparse" in sys.argv
    filename = "sparse.tex" if sparse else "planes.tex"

    s = "\n".join(drawing_code(color_points(), sparse=sparse))

    with open(filename, "w") as f:
        f.write(s)
