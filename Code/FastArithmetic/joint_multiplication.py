from util import w_NAF, right_to_left_scalar_mul
from DataStructures.interfaces import AbstractPoint


class JointMultiplication:

    def __init__(self, point1, point2, w1, w2):
        assert isinstance(point1, AbstractPoint)
        assert isinstance(point2, AbstractPoint)

        self.point1 = point1
        self.point2 = point2

        self.w1 = w1
        self.w2 = w2

        self._P = {}
        self._Q = {}

        # precom stage
        for i in range(1, 2 ** (w1 - 1), 2):
            self._P[i] = right_to_left_scalar_mul(point1, i)
        for j in range(1, 2 ** (w2 - 1), 2):
            self._Q[j] =right_to_left_scalar_mul(point2, j)

        self.precom = (
            (None, self.point2, self.point2.inverse()),
            (self.point1, self.point1.add(self.point2), self.point1.add(self.point2.inverse())),
            (self.point1.inverse(), self.point2.add(self.point1.inverse()), self.point1.inverse().add(self.point2.inverse()))
        )

    def brute_joint_multiplication(self, k, l):
        result1 = right_to_left_scalar_mul(self.point1, k)
        print(result1)
        result2 = right_to_left_scalar_mul(self.point2, l)
        print(result2)
        return result1.add(result2)

    @staticmethod
    def JSF(a, b):
        _u = [[] for i in range(2)]
        d = [0 for i in range(2)]
        _l = [0 for i in range(2)]
        while (a + d[0] > 0) or (b + d[1] > 0):
            _l[0] = d[0] + a
            _l[1] = d[1] + b
            for i in range(2):
                if _l[i] % 2 == 0:
                    u = 0
                else:
                    u = 2 - _l[i] % 4
                    if (_l[i] % 8 == 5 or _l[i] % 8 == 3) and (_l[1-i] % 4 == 2):
                        u = -u
                _u[i].append(u)
            for i in range(2):
                if 2 * d[i] == 1 + _u[i][-1]:
                    d[i] = 1 - d[i]
                if i == 0:
                    #a = floor(a/2)
                    a //= 2
                else:
                    #b = floor(b/2)
                    b //= 2
        return list(reversed(_u[0])), list(reversed(_u[1]))

    def JSF_Multiplication(self, k, l):
        """Add using Shamir Trick, variation of algorithm 3.48, Menezez Book"""
        jsf = self.JSF(k, l)

        #print(jsf)

        R = None

        for i, j in zip(jsf[0], jsf[1]):

            if R is None:
                R = None
            else:
                R = R.point_double()
            if i or j:
                R = self.precom[i][j].add(R)
        return R

    def interleaving_sliding_window(self, k, l):
        """Algorithm 3.5.1 menezez, 'Interleaving with NAF' """

        #_P = {}
       # _Q = {}
        R = None
        naf = [w_NAF(k, self.w1), w_NAF(l, self.w2)]
        #print(naf)
        _l = max([len(naf[0]), len(naf[1])])

        #precom stage
       # for i in range(1, 2**(w1 - 1), 2):
       #     _P[i] = self.point1.right_to_left_scalar_mul(i)
      #  for j in range(1, 2**(w2 - 1), 2):
       #     _Q[j] = self.point2.right_to_left_scalar_mul(j)

        #padding stage
        for i in range(_l - len(naf[0])):
            naf[0].insert(i, 0)
        for i in range(_l - len(naf[1])):
            naf[1].insert(i, 0)

        for i in range(_l):
            if R is None:
                R = None
            else:
                R = R.point_double()
            for j in range(2):
                if naf[j][i] != 0:
                    if naf[j][i] > 0:
                        if j == 0:
                            R = self._P[naf[j][i]].add(R)
                        else:
                            R = self._Q[naf[j][i]].add(R)
                    else:
                        if j == 0:
                            R = self._P[-naf[j][i]].inverse().add(R)
                        else:
                            R = self._Q[-naf[j][i]].inverse().add(R)
        return R


class FastJointMultiplier:
    def __init__(self, point1, point2, w1=4, w2=4):
        assert isinstance(point1, AbstractPoint)
        assert isinstance(point2, AbstractPoint)

        self.point1 = point1
        self.point2 = point2

        self.w1 = w1
        self.w2 = w2

        self._P = {}
        self._Q = {}

        # precom stage
        for i in range(1, 2 ** (w1 - 1), 2):
            self._P[i] = right_to_left_scalar_mul(point1, i)
        for j in range(1, 2 ** (w2 - 1), 2):
            self._Q[j] = right_to_left_scalar_mul(point2, j)

    def interleaving_sliding_window(self, k, l):
        """Algorithm 3.5.1 menezez, 'Interleaving with NAF' """

        R = None
        naf = [w_NAF(k, self.w1), w_NAF(l, self.w2)]
        #print(naf)
        _l = max([len(naf[0]), len(naf[1])])

        #padding stage
        for i in range(_l - len(naf[0])):
            naf[0].insert(i, 0)
        for i in range(_l - len(naf[1])):
            naf[1].insert(i, 0)

        for i in range(_l):
            if R is None:
                R = None
            else:
                R = R.point_double()
            for j in range(2):
                if naf[j][i] != 0:
                    if naf[j][i] > 0:
                        if j == 0:
                            R = self._P[naf[j][i]].add(R)
                        else:
                            R = self._Q[naf[j][i]].add(R)
                    else:
                        if j == 0:
                            R = self._P[-naf[j][i]].inverse().add(R)
                        else:
                            R = self._Q[-naf[j][i]].inverse().add(R)
        return R
