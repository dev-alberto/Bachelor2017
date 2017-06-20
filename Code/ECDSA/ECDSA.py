from DataStructures.PrimeCurves import NistPrimeCurve
from ECDSA.Message import FormatMessage
from util import inv
from FastArithmetic.joint_multiplication import JointMultiplication


class GenerateKeyPair:
    def __init__(self, bits):
        self.curve = NistPrimeCurve(bits)

    def generate_key(self):
        keypair = self.curve.generate_secure_random()
        #assert keypair[1].get_X() != 0
        #return self.curve.generate_secure_random()
        while keypair[1].get_X() == 0:
            keypair = self.curve.generate_secure_random()
        return keypair

class GenerateSignature:
    def __init__(self, bits, keypair, message):
        self.curve = NistPrimeCurve(bits)
        _format = FormatMessage(message, self.curve.n)
        self.z = _format.format()
        self.prvKey = keypair[0]
        self.pubKey = keypair[1]

    def generate_signature(self):
        #r, s = None, None
  #      print("Curve order is ")
   #     print(self.curve.n)
        # while r is None or s is None:
        #     # pasul 4 --> calculam punctul de pe curba eliptica (x1, y1) = k G
        #     #k, point = self.curve.generate_secure_random()
        #     print("k is ")
        #     print(k)
        #
        #     r = point.get_X()
        #     # pasul 5 --> verificam daca r = point.x == 0. Daca e, ne intoarcem la pasul 3
        #     if r == 0:
        #         r = None
        #
        #     print("k^-1")
        #     print(inv(k, self.curve.n))
        #
        #     # pasul 6 --> calculam s = k^-1 ( z + rd_a) mod n
        #     s = (inv(k, self.curve.n) * (self.z + r * self.prvKey)) % self.curve.n
        #     #s = (inv(self.prvKey, self.curve.n) * (self.z + r * self.prvKey)) % self.curve.n
        #     if s == 0:
        #         s = None
        #pasul 4 --> calculam punctul de pe curba eliptica (x1, y1) = k G

 #       print("k is ")
#        print(self.prvKey)

       # print("k^-1")
        #print(inv(self.prvKey, self.curve.n))

        r = self.pubKey.get_X()
        # pasul 6 --> calculam s = k^-1 ( z + rd_a) mod n
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
        muliplier = JointMultiplication(self.curve.g, self.pubKey, 4, 4)
        p = muliplier.interleaving_sliding_window(u1, u2)
        #print("(x1, y1) is " + str(p))

        # pasul 7 --> check signature
        if self.sig[0] == p.get_X():
            return True
        return False
