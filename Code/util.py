from random import randrange
#import math


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


### Fast prime test ###
def isProbablePrime(n, t=7):
    """Miller-Rabin test"""
    def isComposite(a):
        """Check if n is composite"""
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True # n  is definitely composite

    assert n > 0
    if n < 3:
        return [False, False, True][n]
    elif not n & 1:
        return False
    else:
        s, d = 0, n - 1
        while True:
            quotient, remainder = divmod(d, 2)
            if remainder == 1:
                break
            s += 1
            d = quotient
        assert(2**s * d == n-1)
    for _ in range(t):
        if isComposite(randrange(2, n)):
            return False
    return True # no base tested showed n as composite


### Generate random prime ###
def getPrime(n):
    """Get a n-bit prime"""
    from random import getrandbits
    p = getrandbits(n)
    while not isProbablePrime(p):
        p = getrandbits(n)
    return p


#def prime_test(number):
#    if number < 3:
#        return [False, False, True][number]
#    if number % 2 == 0:
#        return False
#    for i in range(3, int(math.sqrt(number)) + 1, 2):
#        if number % i == 0:
#            return False
#    return True


#def bits(n):
#    """
#    Generates the binary digits of n, starting
#    from the least significant bit.

#    bits(151) -> 1, 1, 1, 0, 1, 0, 0, 1
#    """
#    while n:
#        yield n & 1
#        n >>= 1