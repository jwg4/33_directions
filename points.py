import math

from color import get_color


Y = 1.0 / math.sqrt(2.0)


def generate_points():
    for i in range(0, 3):
        yield tuple([0] * i + [1] + [0] * (2 - i))
        yield tuple([1] * i + [0] + [1] * (2 - i))
        yield tuple([Y] * i + [1] + [Y] * (2 - i))
        yield tuple([Y] * i + [-1] + [Y] * (2 - i))
        for j in range(i+1, 3):
            l = [0, 0, 0]
            l[i] = 1
            l[j] = -1
            yield tuple(l)
        for j in range(0, 3):
            if j != i:
                l = [0, 0, 0]
                l[i] = 1
                l[j] = Y
                yield tuple(l)
                l[j] = -Y
                yield tuple(l)
                l = [Y, Y, Y]
                l[i] = 1
                l[j] = -Y
                yield tuple(l)



def color_points():
    for p in generate_points():
        yield (p, get_color(p))
