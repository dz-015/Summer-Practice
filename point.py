from __future__ import annotations
import math

#from line import Line
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
    