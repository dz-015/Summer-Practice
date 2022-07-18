from point import Point
from vector import Vector

class Line():
    def __init__(self, left_point:Point, right_point:Point):
        self.directing_vector:Vector = right_point - left_point
        self.point = left_point
