import math

class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3(x={self.x}, y={self.y}, z={self.z})"

    # Vector addition
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    # Vector subtraction
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    # Scalar multiplication
    def __mul__(self, scalar: float):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    # Scalar division
    def __truediv__(self, scalar: float):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    # Dot product
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Cross product
    def cross(self, other):
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    # Magnitude (length)
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Normalized vector
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0, 0, 0)
        return self / mag
    
    def position(self):
        return f"({self.x},{self.y},{self.z})"