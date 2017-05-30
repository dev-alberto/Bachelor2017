from FastArithmetic.joint_multiplication import JointMultiplication
from time import time
from random import randint
from PerformanceComparison.PerformanceTestInterface import AbstractPerformanceTest


class JointMultiplicationScalarPerformanceTest(AbstractPerformanceTest):
    def __init__(self, iterations, curve, interval, w1, w2, jacobi=False):
        super().__init__(iterations, curve, interval, jacobi=jacobi)
        P = self.curve.generate_random_point()
        Q = self.curve.generate_random_point()
        if jacobi:
            self.joint_mul = JointMultiplication(P.transform_to_Jacobi(), Q.transform_to_Jacobi(), w1, w2)
        else:
            self.joint_mul = JointMultiplication(P, Q, w1, w2)
        #super().__init__(iterations, curve, interval, jacobi=jacobi)

    def brute_force_test(self):
        start = time()
        for i in range(self.iterations):
            scalar1 = randint(self.interval[0], self.interval[1])
            scalar2 = randint(self.interval[0], self.interval[1])
            self.joint_mul.brute_joint_multiplication(scalar1, scalar2)
        return time() - start

    def JSF_mul_test(self):
        start = time()
        for i in range(self.iterations):
            scalar1 = randint(self.interval[0], self.interval[1])
            scalar2 = randint(self.interval[0], self.interval[1])
            self.joint_mul.JSF_Multiplication(scalar1, scalar2)
        return time() - start

    def interleaving_sliding_window_test(self):
        start = time()
        for i in range(self.iterations):
            scalar1 = randint(self.interval[0], self.interval[1])
            scalar2 = randint(self.interval[0], self.interval[1])
            self.joint_mul.interleaving_sliding_window(scalar1, scalar2)
        return time() - start
