from DataStructures.PrimeCurves import NistPrimeCurve
from ECDSA.Message import FormatMessage
from util import inv
from FastArithmetic.joint_multiplication import JointMultiplication


class GenerateKeyPair:
    def __init__(self, bits):
        self.curve = NistPrimeCurve(bits)

    def generate_key(self):
        return self.curve.generate_secure_random()


class GenerateSignature:
    def __init__(self, bits, privKey, message):
        self.curve = NistPrimeCurve(bits)
        _format = FormatMessage(message, self.curve.n)
        self.z = _format.format()
        self.prvKey = privKey

    def generate_signature(self):
        r, s = None, None

        while r is None or s is None:
            # pasul 4 --> calculam punctul de pe curba eliptica (x1, y1) = k G
            k, point = self.curve.generate_secure_random()

            r = point.get_X()
            # pasul 5 --> verificam daca r = point.x == 0. Daca e, ne intoarcem la pasul 3
            if r == 0:
                r = None

            # pasul 6 --> calculam s = k^-1 ( z + rd_a) mod n
            s = (inv(k, self.curve.n) * (self.z + r * self.prvKey)) % self.curve.n
            if s == 0:
                s = None
        return r, s


class VerifySignature:
    def __init__(self, bits, pubKey, sig, message):
        self.curve = NistPrimeCurve(bits)
        _format = FormatMessage(message, self.curve.n)
        self.z = _format.format()
        self.pubKey = pubKey
        self.sig = sig

    def verify(self):
        # pasul 1 --> Check to see signature numbers are in range
        if 1 > self.sig[0] or self.sig[0] >= self.curve.n or 1 > self.sig[0] or self.sig[0] >= self.curve.n:
            return False

            # pasul 4 --> calculam w = s^-1
        w = inv(self.sig[1], self.curve.n)

        # pasul 5 --> calculam u1 = zw mod n si u2 = rw mod n
        u1 = (self.z * w) % self.curve.n
        u2 = (self.sig[0] * w) % self.curve.n

        # pasul 6 --> calculam punctul de pe curba eliptica P = u1 x G + u2 x Q_a  ----> Trebuie optimizat -- Nu mai trebuie
        muliplier = JointMultiplication(self.curve.g, self.pubKey)
        p = muliplier.interleaving_sliding_window(u1, u2, 4, 4)
        # pasul 7 --> check signature
        if self.sig[0] == p.get_X():
            return True
        return False
