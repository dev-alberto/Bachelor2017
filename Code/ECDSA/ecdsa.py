from ECC import Curve
from util import inv
from aritmetica import add_cartesian, scalar_multiplication
from ECDSA import util_ecdsa

#TODO: Create class for ECDSA

curve = Curve(10177, -1, a=1, n=10331, g=[1, 1])

#Alice secret
d_A = util_ecdsa.generate_secure_random(1, curve.n - 1)

#Alice public key
Q_a = scalar_multiplication(curve, curve.g, d_A)


def signature_generation(message):
    #pasul 1 --> calculam hash ul mesajului, unde mesajul este path-ul catre un fisier
    e = util_ecdsa.hash_message(message)

    #pasul 2 --> Truncate Hash
    z = util_ecdsa.truncate_hash(e, curve.n)

    r, s = None, None

    while r is None or s is None:
        # pasul 3 --> generam un random sigur din punct de vedere criptografic in intervalul [1, n-1]
        k = util_ecdsa.generate_secure_random(1, curve.n - 1)

        # pasul 4 --> calculam punctul de pe curba eliptica (x1, y1) = k G
        point = scalar_multiplication(curve, curve.g, k)

        r = point.x
        # pasul 5 --> verificam daca r = point.x == 0. Daca e, ne intoarcem la pasul 3
        if r == 0:
            r = None

        #pasul 6 --> calculam s = k^-1 ( z + rd_a) mod n
        s = (inv(k, curve.n) * (z + r*d_A)) % curve.n
        if s == 0:
            s = None

    return r, s


def verify_signature(sig, message):

    #pasul 1 --> Check to see signature numbers are in range
    if 1 > sig[0] or sig[0] >= curve.n or 1 > sig[0] or sig[0] >= curve.n:
        return False

    #pasul 2 --> La fel ca pasul 1 de la semnare
    e = util_ecdsa.hash_message(message)

    #pasul 3 --> la fel ca pasul 2 de la semnare
    z = util_ecdsa.truncate_hash(e, curve.n)

    #pasul 4 --> calculam w = s^-1
    w = inv(sig[1], curve.n)

    #pasul 5 --> calculam u1 = zw mod n si u2 = rw mod n
    u1 = (z * w) % curve.n
    u2 = (sig[0] * w) % curve.n

    #pasul 6 --> calculam punctul de pe curba eliptica P = u1 x G + u2 x Q_a  ----> Trebuie optimizat
    p = add_cartesian(scalar_multiplication(curve, curve.g, u1), scalar_multiplication(curve, Q_a, u2), curve)

    #pasul 7 --> check signature
    if sig[0] == p.x:
        return True
    return False
