from DataStructures.Points import JacobiPoint
from DataStructures.PrimeCurves import PrimeCurves, NistPrimeCurve
from FastArithmetic.scalar_multiplication import FastScalarMultiplier
from FastArithmetic.joint_multiplication import FastJointMultiplier


class AddWrapeer:
    def __init__(self, x1, y1, x2, y2, a, b, p, nist=False, bits=192):
        if nist:
            self.curve = NistPrimeCurve(bits)
        else:
            self.curve = PrimeCurves(p, b, a)
        self.point1 = JacobiPoint([x1, y1, 1], self.curve)
        self.point2 = JacobiPoint([x2, y2, 1], self.curve)

    def add_wrapper(self):
        return str(self.point1.add(self.point2))


class DoubleWrapper:
    def __init__(self, x, y, a, b, p, nist=False, bits=192):
        if nist:
            self.curve = NistPrimeCurve(bits)
        else:
            self.curve = PrimeCurves(p, b, a)

        self.point = JacobiPoint([x, y, 1], self.curve)

    def double_wrapper(self):
        return str(self.point.point_double())

    def transform_affine_wrapper(self):
        return str(self.point.transform_to_affine())


class ScalarMulWrapper:
    def __init__(self, x, y, a, b, p, scalar, w, nist=False, bits=192):
        if nist:
            self.curve = NistPrimeCurve(bits)
        else:
            self.curve = PrimeCurves(p, b, a)
        self.point = JacobiPoint([x, y, 1], self.curve)
        self.scalar = scalar
        self.multiplier = FastScalarMultiplier(self.point, w)

    def mul_wrapper(self):
        return str(self.multiplier.sliding_window_left_to_right_scalar_mul(self.scalar))


class JointMulWrapper:
    def __init__(self, x1, y1, x2, y2, a, b, p, scalar1, scalar2, w1, w2, nist=False, bits=192):
        if nist:
            self.curve = NistPrimeCurve(bits)
        else:
            self.curve = PrimeCurves(p, b, a)

        self.point1 = JacobiPoint([x1, y1, 1], self.curve)
        self.scalar1 = scalar1
        self.point2 = JacobiPoint([x2, y2, 1], self.curve)
        self.scalar2 = scalar2

        self.multiplier = FastJointMultiplier(self.point1, self.point2, w1, w2)

    def joint_mul_wrapper(self):
        return str(self.multiplier.interleaving_sliding_window(self.scalar1, self.scalar2))

