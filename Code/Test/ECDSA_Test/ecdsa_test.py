from ECDSA import ecdsa


signature = ecdsa.signature_generation("message")

print(ecdsa.verify_signature(signature, "message"))
