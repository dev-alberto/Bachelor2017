from DataStructures.PrimeCurves import P192, P224, P256, P384
from PerformanceComparison.addition import AdditionPerformanceTest

addTest192 = AdditionPerformanceTest(1000, P192)
addTest192J = AdditionPerformanceTest(1000, P192, jacobi=True)

addTest224 = AdditionPerformanceTest(1000, P224)
addTest224J = AdditionPerformanceTest(1000, P224, jacobi=True)

addTest256J = AdditionPerformanceTest(1000, P256, jacobi=True)

addTest384 = AdditionPerformanceTest(1000, P384)
addTest384J = AdditionPerformanceTest(1000, P384, jacobi=True)

print("** 192 **")
#print(addTest192.addition_test())
#print(addTest192.point_double_test())
#print(addTest192J.point_double_test())
#print(addTest192J.addition_test())

#print("** 224 **")
#print(addTest224.addition_test())
print(addTest224J.addition_test())

#print("** 256 **")
#print(addTest256J.addition_test())
#print(addTest256J.point_double_test())

print("** 384 **")
#print(addTest384.addition_test())
#print(addTest384J.addition_test())
#print(addTest384J.point_double_test())