import math

planes = [
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (2, 1),
    (2, -1),
]

FACE_MAPPINGS = {
    (0, 1): [[(-1, -1), (1, 1)], [(0, 0), (1, 1)]],
    (0, -1): [[(1, -1), (-1, 1)], [(0, 2), (1, 3)]],
    (1, 1): [[(1, -1), (-1, 1)], [(0, 1), (1, 2)]],
    (1, -1): [[(-1, -1), (1, 1)], [(-1, 0), (0, 1)]],
    (2, 1): [[(1, -1), (-1, 1)], [(1, 0), (2, 1)]],
    (2, -1): [[(-1, -1), (1, 1)], [(0, -1), (1, 0)]],
}


def plane_intersection(vector, ortho):
    """
        x_dimension = value
        v . ortho = 0
    """
    dimension, value = ortho
    const = 0 - value * vector[dimension]
    coefficients = vector[:dimension] + vector[dimension+1:]
    if all(x == 0 for x in coefficients):
        return None
    return coefficients, const


def _magnitude(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


def _angle(v):
    return math.atan2(v[1], v[0])


def transform(plane, net, line, flip=False):
    """ line is the equation of the line in the plane
        in the form c . v = k
        c_ and k_ are the corresponding constants
        for the transformed equation
        under the mapping which sends the points
        in plane to the points in net.
    """

    if flip:
        plane_d = (plane[0][0] - plane[1][0], plane[1][1] - plane[0][1])
    else:
        plane_d = (plane[1][0] - plane[0][0], plane[1][1] - plane[0][1])
    net_d = (net[1][0] - net[0][0], net[1][1] - net[0][1])
    plane_mag = _magnitude(plane_d)
    net_mag = _magnitude(net_d)
    l = plane_mag / net_mag

    plane_angle = _angle(plane_d)
    net_angle = _angle(net_d)
    th = plane_angle - net_angle
    m = [(l * math.cos(th), - l * math.sin(th)), (l * math.sin(th), l * math.cos(th))]

    if flip:
        a0 = plane[1][0] - (m[0][0] * net[0][0] + m[0][1] * net[0][1]) 
    else:
        a0 = plane[0][0] - (m[0][0] * net[0][0] + m[0][1] * net[0][1]) 
    a1 = plane[0][1] - (m[1][0] * net[0][0] + m[1][1] * net[0][1])
    a = (a0, a1)

    c, k = line
    k_ = k - (c[0] * a[0] + c[1] * a[1])
    c_0 = c[0] * m[0][0] + c[1] * m[1][0] 
    c_1 = c[0] * m[0][1] + c[1] * m[1][1] 
    c_ = (c_0, c_1)

    if abs(c_0) > 0.00001:
        k_ = k_ / c_0
        c_ = (1, c_1 / c_0)
    else:
        k_ = k_ / c_1
        c_ = (0, 1)

    return c_, k_


def get_crossing(line, segment):
    dimension, con, bounds, choose_lower = segment
    c, k = line
    if dimension == 1:
        segment_ = 0, con, bounds, choose_lower
        c_ = (c[1], c[0])
        alternate = get_crossing((c_, k), segment_)
        if alternate:
            alternate = (alternate[1], alternate[0])
        return alternate

    if c[1] == 0:
        cc = k / c[0]
        if cc == con:
            return (con, bounds[1])
        else:
            return None
    
    y = (k - c[0] * con) / c[1]
    if y < bounds[0]:
        return None
    elif y > bounds[1]:
        return None
    elif choose_lower and y == bounds[1]:
        return None
    elif not choose_lower and y == bounds[0]:
        return None
    else:
        return (con, y)


def line_intersecting_square(line, square):
    x_points = [square[0][0], square[1][0]]
    x_bounds = [min(x_points), max(x_points)]
    y_points = [square[0][1], square[1][1]]
    y_bounds = [min(y_points), max(y_points)]
    segments = [
        (0, square[0][0], y_bounds, True),
        (0, square[1][0], y_bounds, False),
        (1, square[0][1], x_bounds, False),
        (1, square[1][1], x_bounds, True),
    ]
    crossing_points = [ get_crossing(line, segment) for segment in segments ]
    return tuple( cp for cp in crossing_points if cp is not None )


def _gen_plane_drawing(vector):
    for plane in planes:
        i = plane_intersection(vector, plane)
        if i:
            cube, net = FACE_MAPPINGS[plane]
            l = transform(cube, net, i)
            points = line_intersecting_square(l, net)
            if points:
                yield points


def plane_drawing(vector):
    return list(_gen_plane_drawing(vector))