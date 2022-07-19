import math

from point import Point
from line import Line


def triangle_area(p1:Point, p2:Point, p3:Point) -> float:
    """Counts area of a trinagle built on its points' coordinates through vector multiplication

    Args:
        p1 (Point): first point
        p2 (Point): second point
        p3 (Point): third point

    Returns:
        float: area of given triangle
    """
    first_vector = p2 - p1
    second_vector = p2 - p3
    vector_multiplication = first_vector * second_vector
    return vector_multiplication.magnitude() / 2

def distance_to_point(left_point:Point, right_point:Point) -> float:
        return math.sqrt((left_point.x - right_point.x)**2 +
                         (left_point.y - right_point.y)**2 +
                         (left_point.z - right_point.z)**2
                         )

def distance_to_line(point:Point, line:Line) -> float:
    vector_to_line = point - line.point
    vector_multiplication = vector_to_line * line.directing_vector
    return vector_multiplication.magnitude() / line.directing_vector.magnitude()