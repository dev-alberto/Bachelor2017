from abc import ABCMeta, abstractmethod


class AbstractPoint(metaclass=ABCMeta):

    def __init__(self, coordinates, curve):
        self.curve = curve
        self.coordinates = coordinates
        super(AbstractPoint, self).__init__()

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def point_double(self):
        pass

    @abstractmethod
    def inverse(self):
        pass

    def right_to_left_scalar_mul(self, d):
        result = None
        R = self
        while d >= 1:
            if d % 2 == 1:
                u = 2 - (d % 4)
                d -= u
                if u == 1:
                    result = R.add(result)
                else:
                    result = R.inverse().add(result)
            d //= 2
            R = R.point_double()
        return result


class EllipticCurve(metaclass=ABCMeta):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass