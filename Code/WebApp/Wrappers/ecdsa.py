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
        #with open('private.pk', 'wb') as f:
         #   dump(self.private, f)
        #with open('public.pk', 'wb') as f:
        #    dump(self.public, f)
        priv = open('keys/private.pk', 'wb')
        dump(self.private, priv)
        pub = open('keys/public.pk', 'wb')
        dump(self.private, pub)
        return priv, pub


class GenerateSigWrapper:

    def __init__(self, bits, pub_path, priv_path, mes):
        with open(pub_path, 'rb') as f:
            pubK = load(f)
        with open(priv_path, 'rb') as f:
            privK = load(f)

        self.gen = GenerateSignature(bits, [privK, pubK], mes)

    def sig_wrapper(self):
        #return str(self.gen.generate_signature())
        sig = open('sig.pk', 'wb')
        dump(self.gen.generate_signature(), sig)
        return sig


class VerifySigWrapper:

    def __init__(self, bits, pub_path, sig_path, mes):
        with open(pub_path, 'rb') as f:
            pubK = load(f)

        with open(sig_path, 'rb') as f:
            sig = load(f)

        self.verifier = VerifySignature(bits, pubK, sig, mes)

    def verify_wrapper(self):
        return str(self.verifier.verify())
