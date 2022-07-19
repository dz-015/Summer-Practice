from point import Point
from vector import Vector

class Line():
    """
    Line consisting of two points saved as directing vector and a point belonging to this line
    """
    def __init__(self, left_point:Point, right_point:Point):
        self.directing_vector:Vector = right_point - left_point
        self.point:Point = left_point
