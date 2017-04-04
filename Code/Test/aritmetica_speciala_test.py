from curve import P192
from FastArithmetic.scalar_multiplication import ScalarMultiplication
from util import w_NAF

generator = P192.get_generator()
#generator = generator.transform()

scalar = 112000

scalar_mul = ScalarMultiplication(generator)
print(scalar_mul.binary_scalar_multiplication(scalar))
#print(scalar_mul.left_to_right_scalar_mul(scalar))
#print(scalar_mul.right_to_left_scalar_mul(scalar))
#print(scalar_mul.window_NAF_multiplication(scalar, 5))
#print(scalar_mul.sliding_window_left_to_right_scalar_mul(scalar))
print(scalar_mul.sliding_window_right_to_left_on_the_fly_scalar_mul(scalar))
