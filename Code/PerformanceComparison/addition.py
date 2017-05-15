from time import time
#from DataStructures.PrimeCurves import NistPrimeCurve
from PerformanceComparison.PerformanceTestInterface import AbstractPerformanceTest


class AdditionPerformanceTest(AbstractPerformanceTest):
    def __init__(self, iterations, curve, jacobi=False):
        if jacobi:
            self.curve.g = self.curve.g.transform_to_Jacobi()
        super().__init__(iterations, curve, None, jacobi=jacobi)

    def addition_test(self):
        start = time()
        for i in range(self.iterations):
            P = self.curve.generate_random_point()
            Q = self.curve.generate_random_point()
            P.add(Q)
        return time() - start

    def point_double_test(self):
        start = time()
        for i in range(self.iterations):
            P = self.curve.generate_random_point()
            P.point_double()
        return time() - start

# P192 = NistPrimeCurve(192)
#
# test = AdditionPerformanceTest(1000, P192, jacobi=True)
# print(test.addition_test())
# print(test.point_double_test())
