from ECC import AbstractPoint
from util import w_NAF, NAF, mods


class ScalarMultiplication:
    def __init__(self, point, w=5):
        assert isinstance(point, AbstractPoint)
        self.point = point
        self.w = w

    ###Multiplicarea cu un scalar in O(logn), in curba C, dP = P + P + ... + P; double and add algorithm###
    ## Algorithm 3.26 Right-to-left binary method for point multiplication ##
    def binary_scalar_multiplication(self, d, special=None):

        if special is None:
            P = self.point
        else:
            P = special

        if d == 0:
            return None  # returnam punctul de la "infinit" daca d este 0
        if d == 1:
            return P

        result = None
        while d > 0:
            if d % 2:
                result = P.add(result)
            d //= 2
            P = P.add(P)
        return result

    ### Left to right NAF scalar multiplication, Geometry, Algebra and Applications: From Mechanics to Cryptography, pagina 126 ###
    ## Menezez Algorithm 3.31 Binary NAF method for point multiplication ##
    def left_to_right_scalar_mul(self, d):
        """:return dP
           :param P : punct de pe o curba eliptica, coordonate Jacobiene
           :param d : scalar
        """

        signed_d = w_NAF(d, 2)

        result = None

        for i in signed_d:
            if result is None:
                result = None
            else:
                result = result.point_double()
            if i == 1:
                result = self.point.add(result)
            if i == -1:
                result = self.point.inverse().add(result)
        return result

    ### Right to left NAF scalar multiplication, signed representation on the fly, works with Affine Coordinates,
    # can be adapted easily for Jacabi coordinates. Algorithm 5 from Mechanics to Cryptography ###
    def right_to_left_scalar_mul(self, d):
        result = None
        R = self.point

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

    #Algorithm 3.36 Window NAF method for point multiplication, Menezez
    def window_NAF_multiplication(self, d, w):

        d = w_NAF(d, w)
        P = self.point
       # print(d)
        _P = {}
        for i in range(1, 2**(w-1), 2):
            _P[i] = self.right_to_left_scalar_mul(i)
        Q = None
        for i in range(0, len(d)):
            if Q is None:
                print("None")
                Q = None
            else:
                Q = Q.point_double()
            if d[i] != 0:
                if d[i] > 0:
                    Q = _P[d[i]].add(Q)
                else:
                    Q = _P[-d[i]].inverse().add(Q)
        return Q


    ### Left to right sliding window NAF, Algorithm 6, Mechanics and Crypyto ###
    # #TODO: SOLVE BIG SCALAR BUG; Posible fix : Algorithm 3.38 Sliding window method for point multiplication
    def sliding_window_left_to_right_scalar_mul(self, d):
        """
        :param P: punct de pe o curba eliptica
        :param d: scalarul
        :param C: curba eliptica
        :return: punctul dP
        """

        #P = self.point

        d = w_NAF(d, 2)
        #print(d)
        Q = None
        i = 0
        m = 2 * ((2 ** self.w - (-1)**self.w) // 3) - 1
        _P = {}
        for _i in range(1, m + 1, 2):
            _P[_i] = self.binary_scalar_multiplication(_i)
        # print(len(_P))
        while i < len(d):
            # print("***")
            # print(d[i])
            if d[i] == 0:
                # print("sdaa")
                if Q is None:
                    Q = None
                else:
                    Q = Q.point_double()
                i += 1
            else:
                s = max(len(d) - i - self.w, 0)
                s = len(d) - 1 - s
                # print(s)
                # print(d[s])
                while d[s] == 0:
                    # print("ds = 0")
                    s -= 1
                #print(d[i:s+1])
                u = NAF(d[i:s + 1])
                # print(s, i)
                # print(u)
                for j in range(1, i - s + 2):
                    # --> modify here with point double
                    Q = Q.point_double()
                if u > 0:
                    Q = _P[u].add(Q)
                    # print("pozitiv")
                if u < 0:
                    #print(u)
                    Q = Q.add(_P[-u].inverse())
                    # print("negativ")
                # print(i, s)
                i = s+1
        return Q

    ### Algorithm 7, Mechanics and Crypto ###
    def sliding_window_right_to_left_on_the_fly_scalar_mul(self, k):

        R = self.point
        m = 2**(self.w-1) - 1
        Q = {}
        for i in range(1, m + 1, 2):
            Q[i] = None
        while k >= 1:
            if k % 2 == 1:
                #t = k % 2**self.w
                t = mods(k, self.w)
                if t > 0:
                    Q[t] = R.add(Q[t])
                if t < 0:
                    Q[-t] = R.inverse().add(Q[-t])
                k -= t
            R = R.point_double()
            k //= 2
        for i in range(3, m + 1, 2):
            if Q[i] is not None:
                Q[1] = self.binary_scalar_multiplication(i, special=Q[i]).add(Q[1])
        return Q[1]
