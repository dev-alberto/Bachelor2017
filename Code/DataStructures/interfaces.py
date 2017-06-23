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


class EllipticCurve(metaclass=ABCMeta):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass
