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
        for j in range(i+1, n-1):
            for d in [20, 40, 60, 80]:
                yield "%s!%d!%s" % (COLORS[i], d, COLORS[j])
        for b in ["white", "black"]:
            for d in [25, 50, 75]:
                yield "%s!%d!%s" % (COLORS[i], d, b)

COLOR_LIST = list(generate_colors())
random.shuffle(COLOR_LIST)
                

def get_color(point):
    return COLOR_LIST.pop()
