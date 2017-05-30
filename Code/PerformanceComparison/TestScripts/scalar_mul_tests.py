from DataStructures.PrimeCurves import P384
from PerformanceComparison.scalar_mul import ScalarMuliplicationPerformanceTest


scalar_mul_jacobi_test192Big = ScalarMuliplicationPerformanceTest(1000, P384, [2**512, 2**600], 4, jacobi=True)

print("SCALAR MUL")
print("*** 192 ***")
#print(scalar_mul_jacobi_test192Big.binary_scalar_mul_test())
#print(scalar_mul_jacobi_test192Big.left_to_right_scalar_mul_test())
#print(scalar_mul_jacobi_test192Big.right_to_left_scalar_mul_test())
print(scalar_mul_jacobi_test192Big.window_naf_mul_test())
print(scalar_mul_jacobi_test192Big.sliding_window_left_to_right_test())
#print(scalar_mul_jacobi_test192Big.sliding_window_right_to_left_test())