from curve import P192, P224, P256, P384
from FastArithmetic.scalar_multiplication import ScalarMultiplication
from random import randint
from time import time


class ScalarMuliplicationPerformanceTest:
    def __init__(self, iterations, curve, interval, jacobi=False):
        self.iterations = iterations
        self.curve = curve
        self.interval = interval
        if jacobi:
            self.scalar_mul = ScalarMultiplication(curve.generate_random_point().transform())
        else:
            self.scalar_mul = ScalarMultiplication(curve.generate_random_point())

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

    def window_naf_mul_test(self, w):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.window_NAF_multiplication(scalar, w)
        return time() - start

    def sliding_window_left_to_right_test(self, w):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.sliding_window_left_to_right_scalar_mul(scalar, w)
        return time() - start

    def sliding_window_right_to_left_test(self, w):
        start = time()
        for i in range(self.iterations):
            scalar = randint(self.interval[0], self.interval[1])
            self.scalar_mul.sliding_window_right_to_left_on_the_fly_scalar_mul(scalar, w)
        return time() - start


# test = ScalarMuliplicationPerformanceTest(1000, P256, [2**256, 2**384])
# print(test.binary_scalar_mul_test())
# print(test.left_to_right_scalar_mul_test())
# print(test.right_to_left_scalar_mul_test())
# print(test.window_naf_mul_test(3))
# #print(test.sliding_window_left_to_right_test(3))
# print(test.sliding_window_right_to_left_test(4))



