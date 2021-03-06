from Code.DataStructures.interfaces import EllipticCurve
from Code.DataStructures.Points import AffinePoint
from Code.curve import get_curve
from Code.util import isProbablePrime


class PrimeCurves(EllipticCurve):
    def __init__(self, prime, b, a, n=None, g=None, h=1):
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
            self.g = AffinePoint(g, self)
        if n is not None:
            self.n = n
        if not isProbablePrime(prime):
            raise ValueError("*** Error *** Characteristic of base field must pe prime")

    def __str__(self):
        return "y^2 = x^3 + " + str(self.a) + "x + " + str(self.b) + " (mod " + str(self.prime) + ")"

    def __eq__(self, other):
        discriminant = -16 * (4 * (self.a ** 3) + 27 * (self.b ** 2)) % self.prime
        other_discriminant = -16 * (4 * (other.a ** 3) + 27 * (other.b ** 2)) % other.prime
        return discriminant == other_discriminant and self.prime == other.prime


class NistPrimeCurve(PrimeCurves):
    def __init__(self, bits):
        params = get_curve(bits)
        self.bits = bits
        super().__init__(params[1], params[2], -3, n=params[3], g=[params[4], params[5]])

    def __str__(self):
        return "P" + str(self.bits)

    def __eq__(self, other):
        return self.bits == other.bits


P192 = NistPrimeCurve(192)
P224 = NistPrimeCurve(224)
P256 = NistPrimeCurve(256)
P384 = NistPrimeCurve(384)
