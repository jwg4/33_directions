def draw_line(a, b, color="black"):
    TEMPLATE = "    \draw[%s] (%.02f,%.02f) -- (%.02f,%.02f);"
    s = TEMPLATE % (color, a[0], a[1], b[0], b[1])
    return s


def draw_point(p, color="black"):
    TEMPLATE = "    \draw[%s] (%.02f,%.02f) circle (1pt);"
    s = TEMPLATE % (color, p[0], p[1])
    return s
