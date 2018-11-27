class Vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if type(other) == type(self):
            return Vec(self.x - other.x, self.y - other.y)
        return Vec(self.x - other, self.y - other)

    def __add__(self, other):
        if type(other) == type(self):
            return Vec(self.x + other.x, self.y + other.y)
        return Vec(self.x + other, self.y + other)

    def __mul__(self, other):
        if type(other) == type(self):
            return Vec(self.x * other.x, self.y * other.y)
        return Vec(self.x * other, self.y * other)

    def __eq__(self, other):
        if type(other) != type(self):
            raise TypeError("Not a vector")
        else:
            return (self.x == other.x and self.y == other.y)

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"


class Directions:
    N = Vec(0, -1)
    S = Vec(0, 1)
    E = Vec(1, 0)
    W = Vec(-1, 0)

    NE = N + E
    NW = N + W
    SE = S + E
    SW = S + W
    NONE = N + S

    ALL = [N, S, E, W, NE, NW, SE, SW, NONE]
    CARDINAL = [N, S, E, W]
