from DataStructures.PrimeCurves import PrimeCurves
from DataStructures.Points import AffinePoint
from FastArithmetic.scalar_multiplication import ScalarMultiplication
from FastArithmetic.joint_multiplication import JointMultiplication

curve = PrimeCurves(97, 2, 3)
P = AffinePoint([10, 16], curve)
Q = AffinePoint([14, 13], curve)

multiplier = ScalarMultiplication(P, 3)

joint_multiplier = JointMultiplication(P, Q, 4, 4)

#print(multiplier.binary_scalar_multiplication(5))
#print(multiplier.left_to_right_scalar_mul(7))
#print(multiplier.window_NAF_multiplication(39))
#print(multiplier.sliding_window_left_to_right_scalar_mul(39))

#print(joint_multiplier.brute_joint_multiplication(5, 6))
#print(joint_multiplier.JSF_Multiplication(21, 26))
#print(joint_multiplier.interleaving_sliding_window(10, 41))
print(joint_multiplier.JSF(21, 26))