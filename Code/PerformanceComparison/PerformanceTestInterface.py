from abc import ABCMeta


class AbstractPerformanceTest(metaclass=ABCMeta):
    def __init__(self, iterations, curve, interval, jacobi=False):
        self.iterations = iterations
        self.curve = curve
        self.interval = interval
        self.jacobi = jacobi
        super(AbstractPerformanceTest, self).__init__()
