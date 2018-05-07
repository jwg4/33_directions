from drawing import draw_line
from geometry import plane_drawing

POINTS = [
    ((1, 0, 0), "green"),
    ((1, 0, 1), "blue"),
    ((1, -1, 0), "red"),
    #((0, -1, -1), "brown"),
]


def drawing_code(points):
    for p, color in points:
        print(p)
        for line in plane_drawing(p):
            print(line, color)
            c = draw_line(*line, color=color)
            yield c


if __name__ == '__main__':
    s = "\n".join(drawing_code(POINTS))
    print(s)