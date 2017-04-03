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


class Point:
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

    def get_point(self):
        return self.x, self.y

    def inverse(self):
        return Point(self.elliptic_curve, [self.x, (self.elliptic_curve.prime - self.y) % self.elliptic_curve.prime])

    def from_cartesian_to_jacobian(self):
        #return (self.x * z**2) % self.elliptic_curve.prime, (self.y * z**3) % self.elliptic_curve.prime, z, z**2, z**3
        return Jacobi_Point([self.x, self.y, 1, 1, 1], self.elliptic_curve)


class Jacobi_Point:
    def __init__(self, coordinates, curve):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.zz = coordinates[3]
        self.zzz = coordinates[4]
        self.curve = curve

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def get_point(self):
        return self.x, self.y, self.z, self.zz, self.zzz

    def inverse(self):
        return Jacobi_Point([self.x, (self.curve.prime - self.y) % self.curve.prime, self.z, self.zz, self.zzz], self.curve)

    def from_jacobi_to_cartesian(self):
        return Point(self.curve, [self.x * inv(self.zz, self.curve.prime) % self.curve.prime, (self.y * inv(self.zzz, self.curve.prime)) % self.curve.prime])



