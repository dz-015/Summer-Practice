import math

class Vector():
    """Provides Vector class defined on its 3 coordinates
    """
    def __init__(self, x:float=0, y:float=0, z:float=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, another_vector):
        """
        Provides vector multiplication
        """
        return Vector((self.y * another_vector.z) - (self.z * another_vector.y),
                     (self.z * another_vector.x) - (self.x * another_vector.z),
                     (self.x * another_vector.y) - (self.y * another_vector.x))
    
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)