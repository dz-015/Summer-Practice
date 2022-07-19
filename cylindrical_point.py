import math

from point import Point


class CylindricalPoint():
    def __init__(self, length:float, angle:float, z_offset:float):
        self.length = length
        self.angle = angle
        self.z_offset = z_offset
    
    def convert(self) -> Point:
        return Point(
            self.length * math.cos(self.angle),
            self.length * math.sin(self.angle),
            self.z_offset
        )