from __future__ import annotations
import math

from line import Line
from vector import Vector

class Point():
    """
    Point in 3-dimensional space
    """
    def __init__(self, x: float=0, y: float=0, z:float=0):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, point) -> Vector:
        """
        Count a Vector from two Points
        """
        return Vector(self.x - point.x,
                     self.y - point.y,
                     self.z - point.z)
    
    def distance_to_point(self, point:Point) -> float:
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)

    def distance_to_line(self, line:Line) -> float:
        vector_to_line = self - line.point
        vector_multiplication = vector_to_line * line.directing_vector
        return vector_multiplication.magnitude() / line.directing_vector.magnitude()



