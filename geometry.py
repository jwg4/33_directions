planes = [
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (2, 1),
    (2, -1),
]


def plane_intersection(vector, ortho):
    """
        x_dimension = value
        v . ortho = 0
    """
    dimension, value = ortho
    const = 0 - value * vector[dimension]
    coefficients = vector[:dimension] + vector[dimension:]
    return coefficients, const