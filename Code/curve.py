from Code.OldCode.ECC import Curve
CURVES = {
    # Bits : (p, order of E(GF(P)), parameter b, base point x, base point y)
    192: (0xfffffffffffffffffffffffffffffffeffffffffffffffff,
          0xffffffffffffffffffffffff99def836146bc9b1b4d22831,
          0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
          0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012,
          0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811),

    224: (0xffffffffffffffffffffffffffffffff000000000000000000000001,
          0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d,
          0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4,
          0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21,
          0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34),

    256: (0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
          0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
          0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
          0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
          0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5),

    384: (0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff,
          0xffffffffffffffffffffffffffffffffffffffffffffffffc7634d81f4372ddf581a0db248b0a77aecec196accc52973,
          0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef,
          0xaa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760ab7,
          0x3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5f),

    521: (6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,
          6864797660130609714981900799081393217269435300143305409394463459185543183397655394245057746333217197532963996371363321113864768612440380340372808892707005449,
          0x051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e16193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00,
          0xc6858e06b70404e9cd9e3ecb662395b4429c648139053fb521f828af606b4d3dbaa14b5e77efe75928fe1dc127a2ffa8de3348b3c1856a429bf97e7e31c2e5bd66,
          0x11839296a789a3bc0045c8a5fb42c7d1bd998f54449579b446817afbd17273e662c97ee72995ef42640c550b9013fad0761353c7086a272c24088be94769fd16650)
    }


def get_curve(bits):
    if bits in CURVES:
        p, n, b, x, y = CURVES[bits]
        return bits, p, b, n, x, y

# #print(get_curve(192))
# p192 = get_curve(192)
# p224 = get_curve(224)
# p256 = get_curve(256)
# p384 = get_curve(384)
# p521 = get_curve(521)
#
# P192 = Curve(p192[1], p192[2], n=p192[3], g=[p192[4], p192[5]])
# P224 = Curve(p224[1], p224[2], n= p224[3], g=[p224[4], p224[5]])
# P256 = Curve(p256[1], p256[2], n=p256[3], g=[p256[4], p256[5]])
# P384 = Curve(p384[1], p384[2], n=p384[3], g=[p384[4], p384[5]])
# #P521 = Curve(p521[0], p521[2], n=p521[3], g=[p521[4], p521[5]])


