from curve import P192, P224, P256, P384
from PerformanceComparison.addition import AdditionPerformanceTest
from PerformanceComparison.scalar_mul import ScalarMuliplicationPerformanceTest
from PerformanceComparison.joint_mul import JointMultiplicationScalarPerformanceTest

add_affine_test192 = AdditionPerformanceTest(1000, P192)
add_affine_test224 = AdditionPerformanceTest(1000, P224)
add_affine_test256 = AdditionPerformanceTest(1000, P256)
add_affine_test384 = AdditionPerformanceTest(1000, P384)
add_jacobi_test192 = AdditionPerformanceTest(1000, P192, jacobi=True)
add_jacobi_test224 = AdditionPerformanceTest(1000, P224, jacobi=True)
add_jacobi_test256 = AdditionPerformanceTest(1000, P256, jacobi=True)
add_jacobi_test384 = AdditionPerformanceTest(1000, P384, jacobi=True)

print("*** 192 ***")
print(add_affine_test192.addition_test())
print(add_affine_test192.point_double_test())
print(add_jacobi_test192.addition_test())
print(add_jacobi_test192.point_double_test())
print("*** 224 ***")
print(add_affine_test224.addition_test())
print(add_affine_test224.point_double_test())
print(add_jacobi_test224.addition_test())
print(add_jacobi_test224.point_double_test())
print("*** 256 ***")
print(add_affine_test256.addition_test())
print(add_affine_test256.point_double_test())
print(add_jacobi_test256.addition_test())
print(add_jacobi_test256.point_double_test())
print("*** 384 ***")
print(add_affine_test384.addition_test())
print(add_affine_test384.point_double_test())
print(add_jacobi_test384.addition_test())
print(add_jacobi_test384.point_double_test())


scalar_mul_affine_test192 = ScalarMuliplicationPerformanceTest(1000, P192, [2**5, 2**32])
scalar_mul_affine_test192Big = ScalarMuliplicationPerformanceTest(1000, P192, [2**128, 2**192])
scalar_mul_jacobi_test192 = ScalarMuliplicationPerformanceTest(1000, P192, [2**5, 2**32], jacobi=True)
scalar_mul_jacobi_test192Big = ScalarMuliplicationPerformanceTest(1000, P192, [2**128, 2**192], jacobi=True)
scalar_mul_jacobi_test224 = ScalarMuliplicationPerformanceTest(1000, P224, [2**5, 2**32], jacobi=True)
scalar_mul_jacobi_test224Big = ScalarMuliplicationPerformanceTest(1000, P224, [2**150, 2**224], jacobi=True)
scalar_mul_jacobi_test256 = ScalarMuliplicationPerformanceTest(1000, P256, [2**5, 2**32], jacobi=True)
scalar_mul_jacobi_test256Big = ScalarMuliplicationPerformanceTest(1000, P256, [2**200, 2**256], jacobi=True)
scalar_mul_jacobi_test384 = ScalarMuliplicationPerformanceTest(1000, P384, [2**5, 2**32], jacobi=True)
scalar_mul_jacobi_test384Big = ScalarMuliplicationPerformanceTest(1000, P384, [2**300, 2**384], jacobi=True)

print("*** 192 ***")
print("binary multiplication")