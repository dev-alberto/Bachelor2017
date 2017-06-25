from unittest import TestCase, main
from DataStructures.Points import AffinePoint, JacobiPoint
from DataStructures.PrimeCurves import PrimeCurves


class AffinePointTest(TestCase):

    def test_add(self):
        curve, point1, point2 = self.createSUT()
        result = point1.add(point2)
        expected_result = AffinePoint([1, 54], curve)
        self.assertEqual(result, expected_result)

    def test_point_double(self):
        curve, point1, point2 = self.createSUT()
        result = point1.point_double()
        expected_result = AffinePoint([32, 90], curve)
        self.assertEqual(result, expected_result)

    def test_inverse(self):
        curve, point1, point2 = self.createSUT()
        result = point1.inverse()
        expected_result = AffinePoint([17, 87], curve)
        self.assertEqual(result, expected_result)

    def test_transform_to_Jacobi(self):
        curve, point1, point2 = self.createSUT()
        result = point1.transform_to_Jacobi()
        expected_result = JacobiPoint([17, 10, 1], curve)
        self.assertEqual(result, expected_result)

    @staticmethod
    def createSUT():
        curve = PrimeCurves(97, 3, 2)
        point1 = AffinePoint([17, 10], curve)
        point2 = AffinePoint([95, 31], curve)
        return curve, point1, point2

if __name__ == '__main__':
    main()
