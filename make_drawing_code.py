# coding=utf-8
import math
import random

from drawing import draw_line, draw_point
from geometry import plane_drawing, antipodes

POINTS = [
    ((1, 0, 0), "green"),
    ((1, 0, 1), "blue"),
    ((1, -1, 0), "red"),
    ((0, -1, -1), "brown"),
]

COLORS = [
    "green",
    "blue",
    "red",
    "brown",
]


def get_color():
    return random.choice(COLORS)


def generate_points():
    y = 1.0 / math.sqrt(2.0)
    for i in range(0, 3):
        yield tuple([0] * i + [1] + [0] * (2 - i))
        for j in range(0, 3):
            if i != j:
                l = [0, 0, 0]
                l[i] = 1
                l[j] = 1
                yield tuple(l)
                l[j] = -1
                yield tuple(l)
                l[j] = y
                yield tuple(l)
                l[j] = -y
                yield tuple(l)
                l = [y, y, y]
                l[i] = 1
                yield tuple(l)
                l[i] = -1
                yield tuple(l)
                l[i] = 1
                l[j] = -y
                yield tuple(l)
                l[i] = -1
                l[j] = -y
                yield tuple(l)


def color_points():
    for p in generate_points():
        yield (p, get_color())


def drawing_code(points):
    for p, color in points:
        for line in plane_drawing(p):
            c = draw_line(*line, color=color)
            yield c
        for point in antipodes(p):
            c = draw_point(point, color=color)
            print(p, point, c)
            yield c


if __name__ == '__main__':
    s = "\n".join(drawing_code(color_points()))
    with open("planes.tex", "w") as f:
        f.write(s)
