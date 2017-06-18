from DataStructures.interfaces import AbstractPoint
from util import inv


class AffinePoint(AbstractPoint):

    def __str__(self):  # Override string conversion used by print and str()
        return "(" + str(self.coordinates[0]) + ", " + str(self.coordinates[1]) + ")"

    def __eq__(self, other):
        return self.coordinates[0] == other.coordinates[0] and self.coordinates[1] == other.coordinates[1]

    def add(self, other):

        #print("add affine")
        if self is None:
            return other
        if other is None:
            return self

        if self == other:
            _lambda = ( (3 * self.coordinates[0] ** 2 + self.curve.a) * inv(2 * self.coordinates[1], self.curve.prime)) % self.curve.prime
        else:
            _lambda = ((other.coordinates[1] - self.coordinates[1]) * inv(other.coordinates[0] - self.coordinates[0], self.curve.prime)) % self.curve.prime
        x3 = (_lambda ** 2 - self.coordinates[0] - other.coordinates[0]) % self.curve.prime
        y3 = (_lambda * (self.coordinates[0] - x3) - self.coordinates[1]) % self.curve.prime
        return AffinePoint([x3, y3], self.curve)

    def point_double(self):
        return self.add(self)

    def get_X(self):
        return self.coordinates[0]

    def get_Y(self):
        return self.coordinates[1]

    def inverse(self):
        return AffinePoint([self.coordinates[0], (self.curve.prime - self.coordinates[1]) % self.curve.prime], self.curve)

    def transform_to_Jacobi(self):
        return JacobiPoint([self.coordinates[0], self.coordinates[1], 1], self.curve)


class JacobiPoint(AbstractPoint):

    def __init__(self, coordinates, curve):
        super().__init__(coordinates, curve)
        self.zz = coordinates[2] ** 2
        self.zzz = coordinates[2] ** 3

    def __str__(self):
        return "(" + str(self.coordinates[0]) + ", " + str(self.coordinates[1]) + ", " + str(self.coordinates[2]) + ")"

    def __eq__(self, other):
        return self.coordinates[0] == other.coordinates[0] and self.coordinates[1] == other.coordinates[1] and self.coordinates[2] == other.coordinates[2]

    def add(self, other):
        #print("Add jacobi")
        if self is None:
            return other
        if other is None:
            return self

        u1 = (self.coordinates[0] * other.zz) % self.curve.prime
        u2 = (other.coordinates[0] * self.zz) % self.curve.prime
        s1 = (self.coordinates[1] * other.zzz) % self.curve.prime
        s2 = (other.coordinates[1] * self.zzz) % self.curve.prime
        if u1 == u2:
            if s1 != s2:
                return None
            else:
                return self.point_double()

        h = (u2 - u1) % self.curve.prime
        r = (s2 - s1) % self.curve.prime
        x3 = (r ** 2 - h ** 3 - 2 * u1 * h ** 2) % self.curve.prime
        y3 = (r * (u1 * h ** 2 - x3) - s1 * h ** 3) % self.curve.prime
        z3 = (h * self.coordinates[2] * other.coordinates[2]) % self.curve.prime
        return JacobiPoint([x3, y3, z3], self.curve)

    def point_double(self):
        if self is None:
            return None
        if self.coordinates[1] == 0:
            return None
        s = (4 * self.coordinates[0] * self.coordinates[1] ** 2) % self.curve.prime
        m = (3 * self.coordinates[0] ** 2 + self.curve.a * self.coordinates[2] ** 4) % self.curve.prime
        _x = (m ** 2 - 2 * s) % self.curve.prime
        _y = (m * (s - _x) - 8 * self.coordinates[1] ** 4) % self.curve.prime
        _z = (2 * self.coordinates[1] * self.coordinates[2]) % self.curve.prime
        return JacobiPoint([_x, _y, _z], self.curve)

    def get_point(self):
        return self.coordinates[0], self.coordinates[1], self.coordinates[2]

    def inverse(self):
        return JacobiPoint([self.coordinates[0], (self.curve.prime - self.coordinates[1]) % self.curve.prime, self.coordinates[2]], self.curve)

    def transform_to_affine(self):
        return AffinePoint([self.coordinates[0] * inv(self.coordinates[2] ** 2, self.curve.prime) % self.curve.prime, (self.coordinates[1] * inv(self.coordinates[2] ** 3, self.curve.prime)) % self.curve.prime], self.curve)