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
    #"green",
    #"blue",
    #"red",
    #"brown",
    #"black!60!green",
    #"black!60!green!40!blue",
    "red!50!yellow!99!blue",
    "yellow!99!blue!50!red",
    "yellow!99!red!50!blue",
]

Y = 1.0 / math.sqrt(2.0)

RATIOS = {
    -Y: 15,
    -1: 30,
    0: 50,
    1: 70,
    Y: 85
}

def get_color(point):
    r0 = RATIOS[point[0]]
    r1 = RATIOS[point[1]]
    r2 = RATIOS[point[2]]
    if point[0] == point[1]:
        return "red!%d!blue!%d!white" % (r0, r2) 
    if point[0] == -point[1]:
        return "red!%d!blue!%d!black" % (r0, r2) 
    if point[1] == point[2]:
        return "red!%d!yellow!%d!white" % (r0, r2) 
    if point[1] == -point[2]:
        return "red!%d!yellow!%d!black" % (r0, r2) 
    if point[0] == point[2]:
        return "blue!%d!yellow!%d!white" % (r0, r1) 
    if point[0] == -point[2]:
        return "blue!%d!yellow!%d!black" % (r0, r1) 
    return "red!%d!white!%d!yellow!%d!blue" % (r0, r1, r2)


def generate_points():
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
                l[j] = Y
                yield tuple(l)
                l[j] = -Y
                yield tuple(l)
                l = [Y, Y, Y]
                l[i] = 1
                yield tuple(l)
                l[i] = -1
                yield tuple(l)
                l[i] = 1
                l[j] = -Y
                yield tuple(l)
                l[i] = -1
                l[j] = -Y
                yield tuple(l)


def color_points():
    for p in generate_points():
        yield (p, get_color(p))


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
