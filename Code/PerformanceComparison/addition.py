from time import time
from PerformanceComparison.PerformanceTestInterface import AbstractPerformanceTest


class AdditionPerformanceTest(AbstractPerformanceTest):
    def __init__(self, iterations, curve, jacobi=False):
        super().__init__(iterations, curve, None, jacobi=jacobi)

    def addition_test(self):
        s = 0
        for i in range(self.iterations):
            P = self.generate_random_point()
            Q = self.generate_random_point()
            start = time()
            P.add(Q)
            s += time() - start
        return s

    def point_double_test(self):
        s = 0
        for i in range(self.iterations):
            P = self.generate_random_point()
            start = time()
            P.point_double()
            s += time() - start
        return s
