from drawing import draw_line
from geometry import plane_drawing

POINTS = [
    (1, 0, 0)
]


def drawing_code(points):
    for p in points:
        for line in plane_drawing(p):
            c = draw_line(*line)
            yield c


if __name__ == '__main__':
    s = "\n".join(drawing_code(POINTS))
    print(s)