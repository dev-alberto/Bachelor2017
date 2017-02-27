import hashlib
from random import SystemRandom


def hash_message(path, buffer=4096):
    """:parameter path : path of file to be hashed
       :parameter buffer : read the file with buffer, in case of large file
       :returns hash of file"""
    m = hashlib.sha256()
    f = open(path, 'rb')
    while True:
        data = f.read(buffer)
        if len(data) == 0: break
        m.update(data)
    f.close()
    return m.digest()


def truncate_hash(h, curve_order):
    e = int.from_bytes(h, byteorder='big')

    #Conform specificatiilor Fips 180, selectam primii z biti de la stanga, unde z reprezinta nr de biti din reprezentarea lui n
    z = e >> (e.bit_length() - curve_order.bit_length())

    return z


def generate_secure_random(start, stop):
    cryptogen = SystemRandom()
    return cryptogen.randrange(start, stop)
