from ECDSA.ECDSA import *


priv, pub = GenerateKeyPair(192).generate_key()

sige = GenerateSignature(192, priv, "ecdsa").generate_signature()

verify = VerifySignature(192, pub, sige, "ecdsa")

print(verify.verify())
