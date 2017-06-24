from abc import ABCMeta
from FastArithmetic.scalar_multiplication import FastScalarMultiplier
from random import randint


class AbstractPerformanceTest(metaclass=ABCMeta):
    def __init__(self, iterations, curve, interval, jacobi=False):
        self.iterations = iterations
        self.curve = curve
        self.interval = interval
        self.jacobi = jacobi
        if jacobi:
            self.multiplier = FastScalarMultiplier(self.curve.g.transform_to_Jacobi())
        else:
            self.multiplier = FastScalarMultiplier(self.curve.g)
        super(AbstractPerformanceTest, self).__init__()

    def generate_random_point(self):
        k = randint(1, self.curve.n-1)
        return self.multiplier.sliding_window_left_to_right_scalar_mul(k)
