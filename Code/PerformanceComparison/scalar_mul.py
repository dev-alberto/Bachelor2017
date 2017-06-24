from FastArithmetic.scalar_multiplication import ScalarMultiplication
from random import randint
from time import time
from PerformanceComparison.PerformanceTestInterface import AbstractPerformanceTest


class ScalarMuliplicationPerformanceTest(AbstractPerformanceTest):
    def __init__(self, iterations, curve, interval, w, jacobi=False):
        super().__init__(iterations, curve, interval, jacobi=jacobi)
        point = self.generate_random_point()
        self.scalar_mul = ScalarMultiplication(point, w)
        #super().__init__(iterations, curve, interval, jacobi=jacobi)

    def binary_scalar_mul_test(self):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.binary_scalar_multiplication(scalar)
        return time() - start

    def left_to_right_scalar_mul_test(self):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.left_to_right_scalar_mul(scalar)
        return time() - start

    def right_to_left_scalar_mul_test(self):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.right_to_left_scalar_mul(scalar)
        return time() - start

    def window_naf_mul_test(self):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.window_NAF_multiplication(scalar)
        return time() - start

    def window_naf_right_to_left_test(self):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.window_NAF_right_to_left(scalar)
        return time() - start

    def sliding_window_left_to_right_test(self):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.sliding_window_left_to_right_scalar_mul(scalar)
        return time() - start



