import random


COLORS = [
    "red",
    "blue",
    "yellow",
    "black"
]


def generate_colors():
    n = len(COLORS)
    for i in range(0, n):
        yield COLORS[i]
        for j in range(i+1, n):
            for d in [15, 30, 50, 70, 85]:
                yield "%s!%d!%s" % (COLORS[i], d, COLORS[j])

COLOR_LIST = list(generate_colors())
random.shuffle(COLOR_LIST)
                

def get_color(point):
    return COLOR_LIST.pop()
