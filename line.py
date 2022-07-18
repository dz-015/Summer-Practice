from point import Point

class Line():
    def __init__(self, left_point:Point, right_point:Point):
        self.directing_vector = right_point - left_point
        self.point = left_point
