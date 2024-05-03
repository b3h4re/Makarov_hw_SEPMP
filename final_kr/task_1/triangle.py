import math


class Triangle(object):
    def __init__(self, a, b, c):
        if self._check_if_exist(a, b, c):
            self.a = a
            self.b = b
            self.c = c

    def _check_if_exist(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        raise ValueError('Треугольник не существует')

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    # ==
    def __eq__(self, other):
        self_sides = sorted([self.a, self.b, self.c])
        other_sides = sorted([other.a, other.b, other.c])
        return self_sides == other_sides

    # !=
    def __ne__(self, other):
        self_sides = sorted([self.a, self.b, self.c])
        other_sides = sorted([other.a, other.b, other.c])
        return self_sides != other_sides

    # <
    def __lt__(self, other) -> bool:
        return self.perimetr() < other.perimetr()

    # >
    def __gt__(self, other) -> bool:
        return self.perimetr() > other.perimetr()

    # <=
    def __le__(self, other) -> bool:
        return self.perimetr() <= other.perimetr()

    # >=
    def __ge__(self, other) -> bool:
        return self.perimetr() >= other.perimetr()

    # *
    def __mul__(self, other):
        self.a *= other
        self.b *= other
        self.c *= other

    def equal(self, other):
        self_sides = sorted([self.a, self.b, self.c])
        other_sides = sorted([other.a, other.b, other.c])
        return self_sides[0] / other_sides[0] == self_sides[1] / other_sides[1] == self_sides[2] / other_sides[2]

    def is_right_angled(self) -> bool:
        return self.a ** 2 + self.b ** 2 == self.c ** 2

    def is_right_triangle(self) -> bool:
        return self.a == self.b == self.c

    def two_sides_eq(self) -> bool:
        return self.a == self.b or self.a == self.c or self.b == self.c

    def __del__(self):
        del self
