from FastArithmetic.scalar_multiplication import ScalarMultiplication
from FastArithmetic.joint_multiplication import JointMultiplication
from DataStructures.Points import JacobiPoint
from DataStructures.PrimeCurves import NistPrimeCurve

from random import randint

P192 = NistPrimeCurve(192)


# generator = P192.get_generator()
# generator = generator.transform()
#
scalar1 = randint(1, P192.n-1)
print(scalar1)
scalar2 = randint(1, P192.n - 1)
print(scalar2)
ab = scalar1 * scalar2

scalar_mul = ScalarMultiplication(P192.g, 4)
print(scalar_mul.sliding_window_left_to_right_scalar_mul(scalar1))
print(scalar_mul.sliding_window_left_to_right_scalar_mul(scalar2))
print(scalar_mul.sliding_window_left_to_right_scalar_mul(ab))

# generator_times2 = P192.g.right_to_left_scalar_mul(2)
# joint_mul = JointMultiplication(P192.g, generator_times2)
#
# print(joint_mul.brute_joint_multiplication(5000, 50001219992343243232))
# print(joint_mul.JSF_Multiplication(5000, 50001219992343243232))
# print(joint_mul.interleaving_sliding_window(5000, 50001219992343243232, 4, 5))





# P192 = NistPrimeCurve(384)
# Paf = P192.g.right_to_left_scalar_mul(3)
# Qaf = P192.g.right_to_left_scalar_mul(5)
# print(Paf.add(Qaf))
#
# P192.g = P192.g.transform_to_Jacobi()
# P = P192.g.right_to_left_scalar_mul(3)
# Q = P192.g.right_to_left_scalar_mul(5)
#
# print(P.add(Q).transform_to_affine())

