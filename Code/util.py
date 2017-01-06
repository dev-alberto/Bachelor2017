####### Euclid #######
def gcd_extended(a, b):
    """ax + by = gcd(a, b)
    :return (x, y, gcd(a,b))"""
    s, old_s, t, old_t, r, old_r = 0, 1, 1, 0, b, a
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t, old_r


####### Invers Modular #######
def inv(a, n):
    """Find the modular inverse x, ax = 1 mod n"""

    i = gcd_extended(a, n)[0]
    while i < 0:
        i += n
    return i