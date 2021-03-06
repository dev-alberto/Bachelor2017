from Code.DataStructures.PrimeCurves import P192, P384
from Code.PerformanceComparison.joint_mul import JointMultiplicationScalarPerformanceTest

joint_mul_affine_192_33 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**5, 2**32], 3, 3)
joint_mul_affine_192Big_33 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 3, 3)
joint_mul_affine_192Big_66 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 6, 6)

joint_mul_jacobi_192_33 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**5, 2**32], 3, 3, jacobi=True)
joint_mul_jacobi_192Big_33 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 3, 3, jacobi=True)
joint_mul_jacobi_192Big_34 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 3, 4, jacobi=True)
joint_mul_jacobi_192Big_44 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 4, 4, jacobi=True)
joint_mul_jacobi_192Big_45 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 4, 5, jacobi=True)
joint_mul_jacobi_192Big_55 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 5, 5, jacobi=True)
joint_mul_jacobi_192_66 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**5, 2**32], 6, 6, jacobi=True)
joint_mul_jacobi_192Big_66 = JointMultiplicationScalarPerformanceTest(1000, P192, [2**128, 2**192], 6, 6, jacobi=True)



joint_mul_affine_384_33 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**5, 2**32], 3, 3)
joint_mul_affine_384Big_33 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**128, 2**192], 3, 3)
joint_mul_affine_384Big_66 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**330, 2**384], 6, 6)

joint_mul_jacobi_384_33 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**5, 2**32], 3, 3, jacobi=True)
joint_mul_jacobi_384Big_33 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**330, 2**384], 3, 3, jacobi=True)
joint_mul_jacobi_384Big_34 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**330, 2**384], 3, 4, jacobi=True)
joint_mul_jacobi_384Big_44 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**330, 2**384], 4, 4, jacobi=True)
joint_mul_jacobi_384Big_45 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**330, 2**384], 4, 5, jacobi=True)
joint_mul_jacobi_384Big_55 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**330, 2**384], 5, 5, jacobi=True)
joint_mul_jacobi_384_66 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**5, 2**32], 6, 6, jacobi=True)
joint_mul_jacobi_384Big_66 = JointMultiplicationScalarPerformanceTest(1000, P384, [2**330, 2**384], 6, 6, jacobi=True)

print("*** 192 ***")
print("Brute")
print("Affine Brute")
print(joint_mul_affine_192_33.brute_force_test())
print(joint_mul_affine_192Big_66.brute_force_test())
print("Jacobi Brute")
print(joint_mul_jacobi_192_33.brute_force_test())
print(joint_mul_jacobi_192Big_33.brute_force_test())
print("JSF")
print("Affine JSF")
print(joint_mul_affine_192_33.JSF_mul_test())
print(joint_mul_affine_192Big_66.JSF_mul_test())
print("Jacobi JSF")
print(joint_mul_jacobi_192_33.JSF_mul_test())
print(joint_mul_jacobi_192Big_33.JSF_mul_test())
print("Interleaving")
print("Affine interleaving")
print(joint_mul_affine_192_33.interleaving_sliding_window_test()) #adaugat
print(joint_mul_affine_192Big_66.interleaving_sliding_window_test()) #adaugat
print("Jacobi Interleaving")
print(joint_mul_jacobi_192_66.interleaving_sliding_window_test())
print(joint_mul_jacobi_192Big_66.interleaving_sliding_window_test())
print("DONE")

print("Interleaving different windows test, must be ignored by averages for Big/Small, and algo comparison")
print(joint_mul_jacobi_192Big_33.interleaving_sliding_window_test())
print(joint_mul_jacobi_192Big_34.interleaving_sliding_window_test())
print(joint_mul_jacobi_192Big_44.interleaving_sliding_window_test())
print(joint_mul_jacobi_192Big_45.interleaving_sliding_window_test())
print(joint_mul_jacobi_192Big_55.interleaving_sliding_window_test())
print(joint_mul_jacobi_192Big_66.interleaving_sliding_window_test())
print("***")


print("*** 384 ***")
print("Brute")
print("Affine Brute")
print(joint_mul_affine_384_33.brute_force_test())
print(joint_mul_affine_384Big_66.brute_force_test())
print("Jacobi Brute")
print(joint_mul_jacobi_384_33.brute_force_test())
print(joint_mul_jacobi_384Big_33.brute_force_test())
print("JSF")
print("Affine JSF")
print(joint_mul_affine_384_33.JSF_mul_test())
print(joint_mul_affine_384Big_66.JSF_mul_test())
print("Jacobi JSF")
print(joint_mul_jacobi_384_33.JSF_mul_test())
print(joint_mul_jacobi_384Big_33.JSF_mul_test())
print("Interleaving")
print("Affine interleaving")
print(joint_mul_affine_384_33.interleaving_sliding_window_test()) #adaugat
print(joint_mul_affine_384Big_66.interleaving_sliding_window_test())
print("Jacobi Interleaving")
print(joint_mul_jacobi_384_66.interleaving_sliding_window_test())
print(joint_mul_jacobi_384Big_66.interleaving_sliding_window_test())
print("DONE")

print("Interleaving different windows test, must be ignored by averages for Big/Small, and algo comparison")
print(joint_mul_jacobi_384Big_33.interleaving_sliding_window_test())
print(joint_mul_jacobi_384Big_34.interleaving_sliding_window_test())
print(joint_mul_jacobi_384Big_44.interleaving_sliding_window_test())
print(joint_mul_jacobi_384Big_45.interleaving_sliding_window_test())
print(joint_mul_jacobi_384Big_55.interleaving_sliding_window_test())
print(joint_mul_jacobi_384Big_66.interleaving_sliding_window_test())
print("***")
