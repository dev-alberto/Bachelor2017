from FastArithmetic.joint_multiplication import JointMultiplication
from time import time
from random import randint


class JointMultiplicationScalarPerformanceTest:
    def __init__(self, iterations, curve, interval, jacobi=False):
        self.iterations = iterations
        self.curve = curve
        self.interval = interval
        P = self.curve.generate_random_point()
        Q = self.curve.generate_random_point()
        if jacobi:
            self.joint_mul = JointMultiplication(P.transform_to_Jacobi(), Q.transform_to_Jacobi())
        else:
            self.joint_mul = JointMultiplication(P, Q)

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

    def interleaving_sliding_window_test(self, w1, w2):
        start = time()
        for i in range(self.iterations):
            scalar1 = randint(self.interval[0], self.interval[1])
            scalar2 = randint(self.interval[0], self.interval[1])
            self.joint_mul.interleaving_sliding_window(scalar1, scalar2, w1, w2)
        return time() - start


# test = JointMultiplicationScalarPerformanceTest(1000, P256, [2**256, 2**384], jacobi=True)
# #print(test.brute_force_test())
# print(test.JSF_mul_test())
# print(test.interleaving_sliding_window_test(3, 3))
