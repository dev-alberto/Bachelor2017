from hashlib import sha256


class FormatMessage:
    def __init__(self, message, curve_order):
        self.curve_order = curve_order
        m = sha256()
        m.update(message.encode())
        self.h = m.digest()

    def format(self):
        e = int.from_bytes(self.h, byteorder='big')

        z = e >> (e.bit_length() - self.curve_order.bit_length())

        return z
