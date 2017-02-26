#Fie o curba eliptica y**2 = x**3 + ax + b mod n  (deci putem reprezenta o curba eliptica printr-un tuplu (a, b, n))
#Vom reprezenta un punct P de pe curba eliptica in coordonate carteziene, folosind o tupla (x, y), x, y numere intregi pozitive

from ECC import Point, Curve, Jacobi_Point
from util import inv


####### Adunarea a 2 puncte in coordonate carteziene, dupa formula #######

def add_cartesian(P1, P2, C):
    #assert isinstance(P1, Point) and isinstance(P2, Point) and isinstance(C, Curve)
    #_lambda = 0

    if P1 is None:
        return P2
    if P2 is None:
        return P1

    if P1 == P2:
        _lambda = ((3 * P1.x ** 2 + C.a) * inv(2 * P1.y, C.prime)) % C.prime
    else:
        _lambda = ((P2.y - P1.y) * inv(P2.x - P1.x, C.prime)) % C.prime
    x3 = (_lambda ** 2 - P1.x - P2.x) % C.prime
    y3 = (_lambda * (P1.x - x3) - P1.y) % C.prime
    return Point(C, [x3, y3])


####### Calculam 2P, unde P un punct in coordonate Jacobi #######

def point_double(P, C):
   # assert isinstance(P, Jacobi_Point) and isinstance(C, Curve)
    if P is None:
        return None
    if P.y == 0:
        return None
    s = (4 * P.x * P.y**2) % C.prime
    m = (3 * P.x**2 + C.a * P.z**4) % C.prime
    _x = (m**2 - 2*s) % C.prime
    _y = (m * (s - _x) - 8 * P.y**4) % C.prime
    _z = (2 * P.y * P.z) % C.prime
    return Jacobi_Point([_x, _y, _z, _z**2 % C.prime, _z**3 % C.prime], C)


# Adunarea a 2 puncte, coordonate Jacobi,
# ne scapa de inversul modular de la adunarea clasica

def add_jacobi(P1, P2, C):
   # assert isinstance(P1, Jacobi_Point) and isinstance(P2, Jacobi_Point) and isinstance(C, Curve)
    if P1 is None:
        return P2
    if P2 is None:
        return P1
    u1 = (P1.x * P2.z**2) % C.prime
    u2 = (P2.x * P1.z**2) % C.prime
    s1 = (P1.y * P2.z**3) % C.prime
    s2 = (P2.y * P1.z**3) % C.prime
    if u1 == u2:
        if s1 != s2:
            return None
        else:
            return point_double(P1, C)
    h = (u2 - u1) % C.prime
    r = (s2 - s1) % C.prime
    x3 = (r**2 - h**3 - 2 * u1 * h**2) % C.prime
    y3 = (r * (u1 * h**2 - x3) - s1 * h**3) % C.prime
    z3 = (h * P1.z * P2.z) % C.prime
    return Jacobi_Point([x3, y3, z3, z3**2 % C.prime, z3**3 % C.prime], C)


###Multiplicarea cu un scalar in O(logn), in curba C, dP = P + P + ... + P###

def scalar_multiplication(C, P, d):
  #  assert isinstance(C, Curve) and isinstance(P, Point)
    if d == 0:
        return None #returnam punctul de la "infinit" daca d este 0
    if d == 1:
        return P
    result = None
    while d > 0:
        if d % 2:
            result = add_cartesian(result, P, C)
        d //= 2
        P = add_cartesian(P, P, C)
    return result


### Generarea w-NAF, articol Signed Binary Representations Revisited, pagina 5 ####
def w_NAF(d, w):
    i = 0
    res = []
    while d >= 1:
        if d % 2 == 0:
            res.append(0)
        else:
            res.append(2 - d % 2 ** w)
            d -= res[i]
        d //= 2
        i += 1
    return res[::-1]


### Left to right NAF scalar multiplication, Geometry, Algebra and Applications: From Mechanics to Cryptography, pagina 126 ###
def left_to_right_scalar_mul(P, d, C):
    """:return dP
     :param P : punct de pe o curba eliptica
     :param d : scalar"""

#    assert isinstance(P, Jacobi_Point) and isinstance(Curve, C)

    signed_d = w_NAF(d, 2)

    result = None

    for i in signed_d:
        result = point_double(result, C)
        if i == 1:
            result = add_jacobi(result, P, C)
        if i == -1:
            result = add_jacobi(result, P.inverse(), C)

    return result


### JSF ###


