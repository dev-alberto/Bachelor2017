from util import inv, isProbablePrime


class Curve:
    """ O curba eliptica in forma Weierstrass"""
    def __init__(self, prime, b, a=-3, n=None, g=None, h=1):
        """a, b --> coeficientii curbei eliptice
            p --> caracteristica corpului peste care este definita curba eliptica
            g --> punctul de baza
            n --> ordinul curbei eliptice
            h --> cofactor
            """
        self.a = a
        self.b = b
        self.prime = prime
        if g is not None:
            self.g = Point(self, g)
        if n is not None:
            self.n = n

        if not isProbablePrime(prime):
            raise ValueError("*** Error *** Characteristic of base field must pe prime")
        self.discriminant = -16 * (4 * (self.a ** 3) + 27 * (self.b ** 2)) % self.prime
        if self.discriminant == 0:
            raise ValueError("*** Error ***: Not an elliptic curve")

    def __str__(self):
        return "y^2 = x^3 + " + str(self.a) + "x + " + str(self.b) + " (mod " + str(self.prime) + ")"

    def __eq__(self, other):
        return self.discriminant == other.discriminant and self.prime == other.prime

    def get_generator(self):
        if self.g is not None:
            return self.g

    @staticmethod
    def scalar_mul(gen, d):
        """Method used in random point generation"""
        result = None
        R = gen
        while d >= 1:
            if d % 2 == 1:
                u = 2 - (d % 4)
                d = d - u
                if u == 1:
                    result = R.add(result)
                else:
                    result = R.inverse().add(result)
            d //= 2
            R = R.point_double()
        return result

    def generate_random_point(self):
        from random import randrange
        if self.n is None or self.g is None:
            raise ValueError("*** Cannot generate random point, curve order must be specified")
        k = randrange(1, self.n-1)
        return self.scalar_mul(self.g, k)


#TODO: use abc module for abstraction
class AbstractPoint:
    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def add(self, other):
        pass

    def point_double(self):
        pass

    def inverse(self):
        pass

    def transform(self):
        pass


class Point(AbstractPoint):
    def __init__(self, elliptic_curve, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.elliptic_curve = elliptic_curve # do maybe a check that ell_curve is instance of class
        # point is on curve
        assert (self.y**2 - self.x**3 - self.elliptic_curve.a * self.x - self.elliptic_curve.b) % self.elliptic_curve.prime == 0

    def __str__(self):  # Override string conversion used by print and str()
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __instancecheck__(self, instance):
        pass

    # def binary_scalar_multiplication(self, d):
    #     P = Point(self.elliptic_curve, [self.x, self.y])
    #     if d == 0:
    #         return None  # returnam punctul de la "infinit" daca d este 0
    #     if d == 1:
    #         return P
    #     result = None
    #     while d > 0:
    #         if d % 2:
    #             result = P + result
    #         d //= 2
    #         P = P + P
    #     return result

    def add(self, other):
        if self is None:
            return other
        if other is None:
            return self

        if self == other:
            _lambda = ((3 * self.x ** 2 + self.elliptic_curve.a) * inv(2 * self.y, self.elliptic_curve.prime)) % self.elliptic_curve.prime
        else:
            _lambda = ((other.y - self.y) * inv(other.x - self.x, self.elliptic_curve.prime)) % self.elliptic_curve.prime
        x3 = (_lambda ** 2 - self.x - other.x) % self.elliptic_curve.prime
        y3 = (_lambda * (self.x - x3) - self.y) % self.elliptic_curve.prime
        return Point(self.elliptic_curve, [x3, y3])

    def point_double(self):
        return self.add(self)

    def get_point(self):
        return self.x, self.y

    def inverse(self):
        return Point(self.elliptic_curve, [self.x, (self.elliptic_curve.prime - self.y) % self.elliptic_curve.prime])

    def transform(self):
        #return (self.x * z**2) % self.elliptic_curve.prime, (self.y * z**3) % self.elliptic_curve.prime, z, z**2, z**3
        return Jacobi_Point([self.x, self.y, 1, 1, 1], self.elliptic_curve)


class Jacobi_Point(AbstractPoint):
    def __init__(self, coordinates, curve):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.zz = coordinates[3]
        self.zzz = coordinates[4]
        self.curve = curve

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def add(self, other):
        if self is None:
            return other
        if other is None:
            return self

        u1 = (self.x * other.z ** 2) % self.curve.prime
        u2 = (other.x * self.z ** 2) % self.curve.prime
        s1 = (self.y * other.z ** 3) % self.curve.prime
        s2 = (other.y * self.z ** 3) % self.curve.prime
        if u1 == u2:
            if s1 != s2:
                return None
            else:
                return self.point_double()

        h = (u2 - u1) % self.curve.prime
        r = (s2 - s1) % self.curve.prime
        x3 = (r ** 2 - h ** 3 - 2 * u1 * h ** 2) % self.curve.prime
        y3 = (r * (u1 * h ** 2 - x3) - s1 * h ** 3) % self.curve.prime
        z3 = (h * self.z * other.z) % self.curve.prime
        return Jacobi_Point([x3, y3, z3, pow(z3, 2, self.curve.prime), pow(z3, 3, self.curve.prime)], self.curve)

    def point_double(self):
        if self is None:
            return None
        if self.y == 0:
            return None
        s = (4 * self.x * self.y ** 2) % self.curve.prime
        m = (3 * self.x ** 2 + self.curve.a * self.z ** 4) % self.curve.prime
        _x = (m ** 2 - 2 * s) % self.curve.prime
        _y = (m * (s - _x) - 8 * self.y ** 4) % self.curve.prime
        _z = (2 * self.y * self.z) % self.curve.prime
        return Jacobi_Point([_x, _y, _z, pow(_z, 2, self.curve.prime), pow(_z, 3, self.curve.prime)], self.curve)

    # def binary_scalar_mul(self, d):
    #     P = Jacobi_Point([self.x, self.y, self.z, self.zz, self.zzz], self.curve)
    #     if d == 0:
    #         return None  # returnam punctul de la "infinit" daca d este 0
    #     if d == 1:
    #         return P
    #     result = None
    #     while d > 0:
    #         if d % 2:
    #             result = P + result
    #         d //= 2
    #         P = P + P
    #     return result

    def get_point(self):
        return self.x, self.y, self.z, self.zz, self.zzz

    def inverse(self):
        return Jacobi_Point([self.x, (self.curve.prime - self.y) % self.curve.prime, self.z, self.zz, self.zzz], self.curve)

    def transform(self):
        return Point(self.curve, [self.x * inv(self.zz, self.curve.prime) % self.curve.prime, (self.y * inv(self.zzz, self.curve.prime)) % self.curve.prime])



