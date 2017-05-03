from curve import P192, P224, P256, P384
from time import time


class AdditionPerformanceTest:
    def __init__(self, iterations, curve, jacobi=False):
        self.iterations = iterations
        self.curve = curve
        if jacobi:
            self.curve.g = self.curve.get_generator().transform()

    def addition_test(self):
        start = time()
        for i in range(self.iterations):
            P = self.curve.generate_random_point()
            Q = self.curve.generate_random_point()
            P.add(Q)
        return time() - start

    def apoint_double_test(self):
        start = time()
        for i in range(self.iterations):
            P = self.curve.generate_random_point()
            P.point_double()
        return time() - start


# test = AdditionPerformanceTest(100, P256, jacobi=True)
# print(test.addition_test())
# print(test.point_double_test())
