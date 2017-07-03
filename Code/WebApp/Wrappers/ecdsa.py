from ECDSA.ECDSA import GenerateKeyPair, VerifySignature, GenerateSignature
from pickle import dump, load


class GenerateKeysWrapper:

    def __init__(self, bits):
        self.gen = GenerateKeyPair(bits)
        self.private, self.public = self.gen.generate_key()

    def gen_private_wrapper(self):
        return str(self.private)

    def gen_public_wrapper(self):
        return str(self.public)

    def serialize_key(self):
        serKey = open('keyPair.pk', 'w')
        with open('keyPair.pk', 'wb') as f:
            dump([self.private, self.public], f)



class GenerateSigWrapper:

    def __init__(self, bits, path, mes):
        with open(path, 'rb') as f:
            keypair = load(f)
        self.gen = GenerateSignature(bits, keypair, mes)

    def sig_wrapper(self):
        return str(self.gen.generate_signature())


class VerifySigWrapper:

    def __init__(self, bits, pubk, sig, mes):
        self.verifier = VerifySignature(bits, pubk, sig, mes)

    def verify_wrapper(self):
        return str(self.verifier.verify())
