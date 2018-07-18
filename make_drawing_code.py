from drawing import draw_line
from geometry import plane_drawing

POINTS = [
    ((1, 0, 0), "green"),
    ((1, 0, 1), "blue"),
    ((1, -1, 0), "red"),
    ((0, -1, -1), "brown"),
]


def drawing_code(points):
    for p, color in points:
        for line in plane_drawing(p):
            c = draw_line(*line, color=color)
            yield c


if __name__ == '__main__':
    s = "\n".join(drawing_code(POINTS))
    with open("planes.tex", "w") as f:
        f.write(s)
