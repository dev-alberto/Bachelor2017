#Fie o curba eliptica y**2 = x**3 + ax + b mod n  (deci putem reprezenta o curba eliptica printr-un tuplu (a, b, n))
#Vom reprezenta un punct P de pe curba eliptica in coordonate carteziene, folosind o tupla (x, y), x, y numere intregi pozitive

from ECC import Point, Curve, Jacobi_Point
from util import inv


####### Verificam daca punctul P apartine curbei #######

def is_on_curve(P, C):
    #assert isinstance(P, Point) and isinstance(C, Curve)
    if isinstance(P, Point) and isinstance(C, Curve):
        return (P.y**2) % C.n == (P.x**3 + C.a * P.x + C.b) % C.n
    print("Provide valid arguments")


####### Adunarea a 2 puncte in coordonate carteziene, dupa formula #######

def add_cartesian(P1, P2, C):
    assert isinstance(P1, Point) and isinstance(P2, Point) and isinstance(C, Curve)
    #_lambda = 0
    if P1 == P2:
        _lambda = ((3 * P1.x ** 2 + C.a) * inv(2 * P1.y, C.n)) % C.n
    else:
        _lambda = ((P2.y - P1.y) * inv(P2.x - P1.x, C.n)) % C.n
    x3 = (_lambda ** 2 - P1.x - P2.x) % C.n
    y3 = (_lambda * (P1.x - x3) - P1.y) % C.n
    return x3, y3


####### Calculam 2P, unde P un punct in coordonate Jacobi #######

def point_double(P, C):
    assert isinstance(P, Jacobi_Point) and isinstance(C, Curve)
    if P.y == 0:
        return None
    s = (4 * P.x * P.y**2) % C.n
    m = (3 * P.x**2 + C.a * P.z**4) % C.n
    _x = (m**2 - 2*s) % C.n
    _y = (m * (s - _x) - 8 * P.y**4) % C.n
    _z = (2 * P.y * P.z) % C.n
    return _x, _y, _z, _z**2 % C.n, _z**3 % C.n


# Adunarea a 2 puncte, coordonate Jacobi,
# ne scapa de inversul modular de la adunarea clasica

def add_jacobi(P1, P2, C):
    assert isinstance(P1, Jacobi_Point) and isinstance(P2, Jacobi_Point) and isinstance(C, Curve)
    u1 = (P1.x * P2.z**2) % C.n
    u2 = (P2.x * P1.z**2) % C.n
    s1 = (P1.y * P2.z**3) % C.n
    s2 = (P2.y * P1.z**3) % C.n
    if u1 == u2:
        if s1 != s2:
            return None
        else:
            return point_double(P1, C)
    h = (u2 - u1) % C.n
    r = (s2 - s1) % C.n
    x3 = (r**2 - h**3 - 2 * u1 * h**2) % C.n
    y3 = (r * (u1 * h**2 - x3) - s1 * h**3) % C.n
    z3 = (h * P1.z * P2.z) % C.n
    return x3, y3, z3, z3**2 % C.n, z3**3 % C.n


###Multiplicarea cu un scalar in O(logn), in curba C, dP = P + P + ... + P###

def scalar_multiplication(C, P, d):
    assert isinstance(C, Curve) and isinstance(P, Point)
    if d == 0:
        return None #returnam punctul de la "infinit" daca d este 0
    if d == 1:
        return P
    result = Point(None, None)
    while d > 0:
        if d % 2:
            result = add_cartesian(result, P, C)
        d //= 2
        P = add_cartesian(P, P, C)
    return result


### Generarea w-NAF ####
def w_NAF(d, w):
    i = 0
    res = []
    while d >= 1:
        if d % 2 == 0:
            res.append(0)
        else:
            res.append(d % 2**w)
            d -= res[i]
        d //= 2
        i += 1
    return res[::-1]


### JSF ###


