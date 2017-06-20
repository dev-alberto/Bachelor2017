from ECDSA.ECDSA import *


keypair = GenerateKeyPair(192).generate_key()

print("Private Key")
print(keypair[0])

print("Public key")
print(keypair[1])

sige = GenerateSignature(192, keypair, "ECDSA Test").generate_signature()

print("Signature")

print(sige)

verify = VerifySignature(192, keypair[1], sige, "ECDSA Test")

print(verify.verify())
