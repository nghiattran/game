import math


class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("This "+str(key)+" key is not a vector key!")

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            # Vector multiplication
            return self.x * other.x + self.y * other.y
        else:
            # Scalar multiplication
            return Vector2D(self.x * other, self.y * other)

    def __cmp__(self, other):
        if self.x == object.x and self.y == other.y:
            return True
        return False

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__

    def get_angle(self, other, radians=False):
        """Will return the angle between this vector and the other vector."""
        if self.length() == 0 or other.length() == 0:
            return 0
        if not radians:
            return (360 / (2 * math.pi)) * (math.atan2(other.y, other.x) - math.atan2(self.y, self.x))
        else:
            return math.atan2(other.y, other.x) - math.atan2(self.y, self.x)

    def normalize(self): # divides a vector by its length
        l = self.length()
        if l != 0:
            return (self.x / l, self.y / l)
        return None

    def length(self): # get length (used for normalize)
        return math.sqrt((self.x**2 + self.y**2))

    def get(self):
        return (self.x, self.y)

    def div(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __len__(self):
        return round(math.sqrt(self.x**2 + self.y**2))