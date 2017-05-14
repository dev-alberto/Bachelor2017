#Fie o curba eliptica y**2 = x**3 + ax + b mod n  (deci putem reprezenta o curba eliptica printr-un tuplu (a, b, n))
#Vom reprezenta un punct P de pe curba eliptica in coordonate carteziene, folosind o tupla (x, y), x, y numere intregi pozitive

from OldCode.ECC import Point, Jacobi_Point
from util import inv

#THIS IS DEPRECATED AND WILL BE DELETED in DUE TIME

####### Adunarea a 2 puncte in coordonate carteziene, dupa formula #######
#added in Class
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
#added in Class
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
#added in Class
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


###Multiplicarea cu un scalar in O(logn), in curba C, dP = P + P + ... + P; double and add algorithm###
#added in Class
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
     :param P : punct de pe o curba eliptica, coordonate Jacobiene
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


### Right to left NAF scalar multiplication, signed representation on the fly, works with Affine Coordinates,
# can be adapted easily for Jacabi coordinates. Algorithm 5 from Mechanics to Cryptography ###
def right_to_left_scalar_mul(P, d, C):
    """:return dP
    :parameter d: scalar
    :parameter P: punct de pe o curba eliptica, in coordonate afine"""

    result = None

    R = Point(C, list(P.get_point()))
    #works also with R = P, which is weird

    while d >= 1:
        if d % 2 == 1:
            u = 2 - (d % 4)
            d = d - u
            if u == 1:
                result = add_cartesian(result, R, C)
            else:
                result = add_cartesian(result, R.inverse(), C)
        d //= 2
        R = add_cartesian(R, R, C)
    return result

def NAF(k):
    s = 0
    for i in range(len(k)):
        s += k[i] * 2**(len(k)-i-1)
    return s


### Left to right sliding window NAF, Algorithm 6, Mechanics and Crypyto ###
def sliding_window_left_to_right_scalar_mul(P, d, w, C):
    """
    :param P: punct de pe o curba eliptica
    :param d: scalarul
    :param C: curba eliptica
    :return: punctul dP
    """
    d = w_NAF(d, w)
    Q = None
    i = 0
    m = 2*((2**w - (-1)**w) // 3) - 1
    _P = {}
    for _i in range(1, m+1, 2):
        _P[_i] = precom(_i, P, C)
    #print(len(_P))
    while i < len(d):
        #print("***")
        #print(d[i])
        if d[i] == 0:
            #print("sdaa")
            Q = add_jacobi(Q, Q, C)
            i += 1
        else:
            s = max(len(d) - i - w, 0)
            s = len(d) - 1 - s
            #print(s)
            #print(d[s])
            while d[s] == 0:
                #print("ds = 0")
                s -= 1
            #print(d[i:s+1])
            u = NAF(d[i:s+1])
            #print(s, i)
            #print(u)
            for j in range(1, i-s + 2):
                #--> modify here with point double
                Q = add_jacobi(Q, Q, C)
            if u > 0:
                Q = add_jacobi(Q, _P[u], C)
                #print("pozitiv")
            if u < 0:
                #print(u)
                Q = add_jacobi(Q, _P[-u].inverse(), C)
                #print("negativ")
            #print(i, s)
            i = s + 1
    return Q


def precom(k, P, C):
    R = None
    for i in range(k):
        R = add_jacobi(R, P, C)
    return R


### Algorithm 7, Mechanics and Crypto ###
def sliding_window_right_to_left_on_the_fly_scalar_mul(P, k, w, C):
    """
    :param P: Elliptic curve point
    :param k: integer scalar
    :param w: window width
    :param C: elliptic curve
    :return: kP
    """
    R = P
    m = 2**(w-1) - 1
    #indeces = [i for i in range(1, m+1, 2)]
    Q = {}
    for i in range(1, m+1, 2):
        Q[i] = None
    while k >= 1:
        if k % 2 == 1:
            t = k % 2**w
            if t > 0:
                Q[t] = add_jacobi(Q[t], R, C)
            if t < 0:
                Q[-t] = add_jacobi(Q[-t], R.inverse(), C)
            k -= t
        R = point_double(R, C)
        k //= 2
    for i in range(3, m+1, 2):
        Q[1] = add_jacobi(Q[1], precom(i, Q[i], C), C)
    return Q[1]

