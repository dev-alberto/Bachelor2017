from util import inv

N = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def inverse(self):
        return self.x, (N - self.y) % N

    def from_cartesian_to_jacobian(self, z=1):
        return (self.x * z**2) % N, (self.y * z**3) % N, z, z**2, z**3

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Jacobi_Point:
    def __init__(self, x, y, z=1):
        self.x = x
        self.y = y
        self.z = z
        self.zz = z**2
        self.zzz = z**3

    def get_point(self):
        return self.x, self.y, self.z, self.zz, self.zzz

    def inverse(self):
        return self.x, (N - self.y) % N, self.z, self.zz, self.zzz

    def from_jacobi_to_cartesian(self):
        return (self.x * inv(self.zz, N)) % N, (self.y * inv(self.zzz, N)) % N

class Curve:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
