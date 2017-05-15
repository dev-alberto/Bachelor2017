from FastArithmetic.scalar_multiplication import ScalarMultiplication
from FastArithmetic.joint_multiplication import JointMultiplication
from DataStructures.Points import JacobiPoint
from DataStructures.PrimeCurves import NistPrimeCurve

P192 = NistPrimeCurve(192)


# generator = P192.get_generator()
# generator = generator.transform()
#
# scalar = 21212525555
#
# scalar_mul = ScalarMultiplication(generator)
# print(scalar_mul.binary_scalar_multiplication(scalar))
# print(scalar_mul.left_to_right_scalar_mul(scalar))
# print(scalar_mul.right_to_left_scalar_mul(scalar))
# print(scalar_mul.window_NAF_multiplication(scalar, 3))
# print(scalar_mul.sliding_window_left_to_right_scalar_mul(scalar, 3))
# print(scalar_mul.sliding_window_right_to_left_on_the_fly_scalar_mul(scalar, 5))

generator_times2 = P192.g.right_to_left_scalar_mul(2)
joint_mul = JointMultiplication(P192.g, generator_times2)

print(joint_mul.brute_joint_multiplication(5000, 50001219992343243232))
print(joint_mul.JSF_Multiplication(5000, 50001219992343243232))
print(joint_mul.interleaving_sliding_window(5000, 50001219992343243232, 4, 5))





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

