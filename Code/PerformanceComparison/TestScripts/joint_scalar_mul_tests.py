from DataStructures.PrimeCurves import P192
from PerformanceComparison.joint_mul import JointMultiplicationScalarPerformanceTest


joint_mul_jacobi_192Big = JointMultiplicationScalarPerformanceTest(100, P192, [2**128, 2**192], 4, 4, jacobi=True)

print("192")

print(joint_mul_jacobi_192Big.brute_force_test())
print(joint_mul_jacobi_192Big.JSF_mul_test())
print(joint_mul_jacobi_192Big.interleaving_sliding_window_test())

