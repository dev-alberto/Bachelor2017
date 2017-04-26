from math import floor
from FastArithmetic.scalar_multiplication import ScalarMultiplication


class JointMultiplication:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.multiplicator_point1 = ScalarMultiplication(point1)
        self.multiplicator_point2 = ScalarMultiplication(point2)

    def brute_joint_multiplication(self, k, l):
        result1 = self.multiplicator_point1.sliding_window_right_to_left_on_the_fly_scalar_mul(k)
        result2 = self.multiplicator_point2.sliding_window_right_to_left_on_the_fly_scalar_mul(l)
        return result1.add(result2)

    @staticmethod
    def JSF(a, b):
        _u = [[] for i in range(2)]
        d = [0 for i in range(2)]
        _l = [0 for i in range(2)]
        while (a + d[0] > 0) and (b + d[1] > 0):
            #print("***")
            _l[0] = d[0] + a
            _l[1] = d[1] + b
            for i in range(2):
                if _l[i] % 2 == 0:
                    u = 0
                else:
                    u = 2 - _l[i] % 4
                    if (_l[i] % 8 == 5 or _l[i] % 8 == 3) and (_l[1-i] % 4 == 2):
                        #print("sadas")
                        u = -u
                _u[i].append(u)
                #print(k)
            for i in range(2):
                #   print(i)
                #d[i] = (d[i] - _u[i][-1]) // 2
                if 2 * d[i] == 1 + _u[i][-1]:
                    d[i] = 1 - d[i]
                if i == 0:
                    a = floor(a/2)
                else:
                    b = floor(b/2)
        return list(reversed(_u[0])), list(reversed(_u[1]))

    def JSF_Multiplication(self, k, l):
        """Add using Shamir Trick, variation of algorithm 3.48, Menezez Book"""
        jsf = self.JSF(k, l)

        P = self.point1
        Q = self.point2

        R = None

        precom = (
                  (None, Q, Q.inverse()),
                  (P, P.add(Q), P.add(Q.inverse())),
                  (P.inverse(), Q.add(P.inverse()), P.inverse().add(Q.inverse()))
                 )

        for i, j in zip(jsf[0], jsf[1]):
            if R is None:
                R = None
            else:
                R = R.point_double()
            if i or j:
                R = precom[i][j].add(R)
        return R


