from curve import P192, P224, P256, P384
from time import time


def test_addition_affine_coordinates(iterations):

    start192 = time()
    for i in range(iterations):
        P = P192.generate_random_point()
        Q = P192.generate_random_point()
        P.add(Q)
    end192 = time()

    start224 = time()
    for i in range(iterations):
        P = P224.generate_random_point()
        Q = P224.generate_random_point()
        P.add(Q)
    end224 = time()

    start256 = time()
    for i in range(iterations):
        P = P256.generate_random_point()
        Q = P256.generate_random_point()
        P.add(Q)
    end256 = time()

    start384 = time()
    for i in range(iterations):
        P = P384.generate_random_point()
        Q = P384.generate_random_point()
        P.add(Q)
    end384 = time()

    # start521 = time()
    # for i in range(iterations):
    #     P = P521.generate_random_point()
    #     Q = P521.generate_random_point()
    #     P.add(Q)
    # end521 = time()

    return end192 - start192, end224 - start224, end256 - start256, end384 - start384


def test_addition_jacobi_coordinates(iterations):
    g192 = P192.get_generator()
    jacobiGen192 = g192.transform()
    g224 = P224.get_generator()
    jacobiGen224 = g224.transform()
    g256 = P256.get_generator()
    jacobiGen256 = g256.transform()
    g384 = P384.get_generator()
    jacobiGen384 = g384.transform()

    P192.g = jacobiGen192
    P224.g = jacobiGen224
    P256.g = jacobiGen256
    P384.g = jacobiGen384

    start192 = time()
    for i in range(iterations):
        P = P192.generate_random_point()
        Q = P192.generate_random_point()
        P.add(Q)
    end192 = time()

    start224 = time()
    for i in range(iterations):
        P = P224.generate_random_point()
        Q = P224.generate_random_point()
        P.add(Q)
    end224 = time()

    start256 = time()
    for i in range(iterations):
        P = P256.generate_random_point()
        Q = P256.generate_random_point()
        P.add(Q)
    end256 = time()

    start384 = time()
    for i in range(iterations):
        P = P384.generate_random_point()
        Q = P384.generate_random_point()
        P.add(Q)
    end384 = time()

    return end192 - start192, end224 - start224, end256 - start256, end384 - start384


print(test_addition_affine_coordinates(10))
print(test_addition_jacobi_coordinates(10))
