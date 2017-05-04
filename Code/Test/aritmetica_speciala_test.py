from curve import P192
from FastArithmetic.scalar_multiplication import ScalarMultiplication
from FastArithmetic.joint_multiplication import JointMultiplication

generator = P192.get_generator()
#generator = generator.transform()

scalar = 21212525555

scalar_mul = ScalarMultiplication(generator)
print(scalar_mul.binary_scalar_multiplication(scalar))
print(scalar_mul.left_to_right_scalar_mul(scalar))
print(scalar_mul.right_to_left_scalar_mul(scalar))
print(scalar_mul.window_NAF_multiplication(scalar, 3))
print(scalar_mul.sliding_window_left_to_right_scalar_mul(scalar, 3))
print(scalar_mul.sliding_window_right_to_left_on_the_fly_scalar_mul(scalar, 5))

#generator_times2 = scalar_mul.sliding_window_right_to_left_on_the_fly_scalar_mul(2)
#joint_mul = JointMultiplication(generator, generator_times2)
#print(joint_mul.brute_joint_multiplication(1900, 5))
#print(joint_mul.JSF_Multiplication(1900, 5))
#print(joint_mul.interleaving_sliding_window(1900, 5, 4, 5))
