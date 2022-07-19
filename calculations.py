from point import Point
from vector import Vector


def triangle_area(p1:Point, p2:Point, p3:Point):
    """
    Counts area of a trinagle built on its coordinates
    """
    first_vector = p2 - p1
    second_vector = p2 - p3
    vector_multiplication = first_vector * second_vector
    return vector_multiplication.magnitude() / 2