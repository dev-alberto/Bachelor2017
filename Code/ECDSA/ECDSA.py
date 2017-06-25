from DataStructures.PrimeCurves import NistPrimeCurve
from ECDSA.Message import FormatMessage
from util import inv
from FastArithmetic.joint_multiplication import FastJointMultiplier
from FastArithmetic.scalar_multiplication import FastScalarMultiplier
from random import SystemRandom


class GenerateKeyPair:
    def __init__(self, bits):
        self.curve = NistPrimeCurve(bits)
        self.cryptogen = SystemRandom()

    def generate_key(self):
        multiplier = FastScalarMultiplier(self.curve.g)
        k = self.cryptogen.randrange(1, self.curve.n - 1)
        point = multiplier.sliding_window_left_to_right_scalar_mul(k)
        if point.get_X() == 0:
            raise ValueError("Please Generate Keu pair Again")
        return k, point


class GenerateSignature:
    def __init__(self, bits, keypair, message):
        self.curve = NistPrimeCurve(bits)
        _format = FormatMessage(message, self.curve.n)
        self.z = _format.format()
        self.prvKey = keypair[0]
        self.pubKey = keypair[1]

    def generate_signature(self):
        r = self.pubKey.get_X()
        s = (inv(self.prvKey, self.curve.n) * (self.z + r * self.prvKey)) % self.curve.n
        if s == 0:
            raise ValueError("Generate key pair again")
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
        #print("w is " + str(w))

        # pasul 5 --> calculam u1 = zw mod n si u2 = rw mod n
        u1 = (self.z * w) % self.curve.n
        u2 = (self.sig[0] * w) % self.curve.n
        #print("u_1 is " + str(u1))
        #print("u_2 is " + str(u2))

        # pasul 6 --> calculam punctul de pe curba eliptica P = u1 x G + u2 x Q_a  ----> Trebuie optimizat -- Nu mai trebuie
        muliplier = FastJointMultiplier(self.curve.g, self.pubKey)
        p = muliplier.interleaving_sliding_window(u1, u2)
        #print("(x1, y1) is " + str(p))

        # pasul 7 --> check signature
        if self.sig[0] == p.get_X():
            return True
        return False
