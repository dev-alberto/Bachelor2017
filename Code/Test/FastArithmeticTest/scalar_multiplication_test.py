import unittest
from DataStructures.PrimeCurves import PrimeCurves
from DataStructures.Points import AffinePoint
from FastArithmetic.scalar_multiplication import ScalarMultiplication


class ScalarMultiplicationTest(unittest.TestCase):

    def test_binary_scalar_multiplication(self):
        curve, instance, scalar, expected_result = self.createSUT()
        result = instance.binary_scalar_multiplication(scalar)
        self.assertEqual(result, expected_result)

    def test_left_to_right_scalar_mul(self):
        curve, instance, scalar, expected_result = self.createSUT()
        result = instance.binary_scalar_multiplication(scalar)
        self.assertEqual(result, expected_result)

    def test_right_to_left_scalar_mul(self):
        curve, instance, scalar, expected_result = self.createSUT()
        result = instance.binary_scalar_multiplication(scalar)
        self.assertEqual(result, expected_result)

    def test_window_NAF_multiplication(self):
        curve, instance, scalar, expected_result = self.createSUT()
        result = instance.binary_scalar_multiplication(scalar)
        self.assertEqual(result, expected_result)

    def test_window_NAF_right_to_left(self):
        curve, instance, scalar, expected_result = self.createSUT()
        result = instance.binary_scalar_multiplication(scalar)
        self.assertEqual(result, expected_result)

    def test_sliding_window_left_to_right_scalar_mul(self):
        curve, instance, scalar, expected_result = self.createSUT()
        result = instance.binary_scalar_multiplication(scalar)
        self.assertEqual(result, expected_result)

    @staticmethod
    def createSUT():
        curve = PrimeCurves(97, 3, 2)
        point1 = AffinePoint([73, 14], curve)
        instance = ScalarMultiplication(point1, 5)
        scalar = 6
        expected_result = AffinePoint([3, 91], curve)
        return curve, instance, scalar, expected_result

if __name__ == '__main__':
    unittest.main()
