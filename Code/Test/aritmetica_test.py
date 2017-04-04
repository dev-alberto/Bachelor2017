from ECC import Curve, Point
import aritmetica

curve = Curve(97, 3, a=2)
point1 = Point(curve, [17, 10])
point2 = Point(curve, [95, 31])

jacobi_point1 = point1.from_cartesian_to_jacobian()
jacobi_point2 = point2.from_cartesian_to_jacobian()

### cartesian addition test ###

assert aritmetica.add_cartesian(point1, point2, curve) == Point(curve, [1, 54])


### point double test, coordinate transformation test ###

jacobi_result = aritmetica.point_double(jacobi_point1, curve)
assert jacobi_result.from_jacobi_to_cartesian() == Point(curve, [32, 90])

### Jacobi addition test ###


jacobi_res = aritmetica.add_jacobi(jacobi_point1, jacobi_point2, curve)
assert jacobi_res.from_jacobi_to_cartesian() == Point(curve, [1, 54])


### scalar multiplication test ###

assert aritmetica.scalar_multiplication(curve, point1, 3) == Point(curve, [1, 43])


### Left to right NAF Test ###
jacobi_res2 = aritmetica.left_to_right_scalar_mul(jacobi_point1, 3, curve)

assert jacobi_res2.from_jacobi_to_cartesian() == Point(curve, [1, 43])


### Right to left NAF Test ###
cartesian_res = aritmetica.right_to_left_scalar_mul(point1, 4, curve)

assert cartesian_res == Point(curve, [95, 66])

#print(cartesian_res)

### Sliding window, left to right ###
sliding_left_res = aritmetica.sliding_window_left_to_right_scalar_mul(jacobi_point1, 12, 5, curve)
print(sliding_left_res.from_jacobi_to_cartesian())


### Sliding window, right to left ###
sliding_right_res = aritmetica.sliding_window_right_to_left_on_the_fly_scalar_mul(jacobi_point1, 12, 5, curve)
print(sliding_right_res.from_jacobi_to_cartesian())
