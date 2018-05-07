def draw_line(a, b):
    print(a)
    print(b)
    TEMPLATE = "\draw (%.02f,%.02f) -- (%.02f,%.02f);"
    s = TEMPLATE % (a[0], a[1], b[0], b[1])
    return s