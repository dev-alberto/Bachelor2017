from unittest import TestCase, main
from DataStructures.Points import AffinePoint
from DataStructures.PrimeCurves import PrimeCurves
from FastArithmetic.joint_multiplication import JointMultiplication


class JointMultiplicationTest(TestCase):

    def test_brute_joint_multiplication(self):
        instance, expected_result, scalar1, scalar2 = self.createSUT()
        result = instance.brute_joint_multiplication(scalar1, scalar2)
        self.assertEqual(result, expected_result)

    def test_JSF(self):
        pass

    def test_JSF_Multiplication(self):
        instance, expected_result, scalar1, scalar2 = self.createSUT()
        result = instance.JSF_Multiplication(scalar1, scalar2)
        self.assertEqual(result, expected_result)

    def test_nterleaving_sliding_window(self):
        instance, expected_result, scalar1, scalar2 = self.createSUT()
        result = instance.interleaving_sliding_window(scalar1, scalar2)
        self.assertEqual(result, expected_result)

    @staticmethod
    def createSUT():
        curve = PrimeCurves(97, 3, 2)
        point1 = AffinePoint([73, 14], curve)
        point2 = AffinePoint([55, 6], curve)
        instance = JointMultiplication(point1, point2, 5, 4)
        scalar1, scalar2 = 7, 8
        expected_result = AffinePoint([28, 34], curve)
        return instance, expected_result, scalar1, scalar2

if __name__ == '__main__':
    main()
