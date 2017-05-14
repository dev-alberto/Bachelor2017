from curve import P192
from time import time
from DataStructures.PrimeCurves import NistPrimeCurve


class AdditionPerformanceTest:
    def __init__(self, iterations, curve, jacobi=False):
        self.iterations = iterations
        self.curve = curve
        if jacobi:
            self.curve.g = self.curve.g.transform_to_Jacobi()

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

P256 = NistPrimeCurve(192)

test = AdditionPerformanceTest(100, P256)
print(test.addition_test())
# print(test.point_double_test())
