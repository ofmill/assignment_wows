import math
from sources.paint.common.Coordinates import Coordinates


def points_diff(point_b: Coordinates, point_a: Coordinates):
    return Coordinates(point_b.x - point_a.x, point_b.y - point_a.y)


def dot_product(vector_a: Coordinates, vector_b: Coordinates):
    return vector_a.x * vector_b.x + vector_a.y * vector_b.y


def two_points_length(point_a: Coordinates, point_b: Coordinates):
    return math.sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2)


def vector_length(vector_a: Coordinates):
    return math.sqrt(vector_a.x ** 2 + vector_a.y ** 2)


def compute_angle(vertex: Coordinates, point_a: Coordinates, point_b: Coordinates) -> float:
    vector_a = points_diff(point_a, vertex)
    vector_b = points_diff(point_b, vertex)
    return math.degrees(math.acos(dot_product(vector_a, vector_b) /
                                  (vector_length(vector_a) * vector_length(vector_b))))
