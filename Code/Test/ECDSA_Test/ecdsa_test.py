from unittest import TestCase
from ECDSA.ECDSA import GenerateSignature, GenerateKeyPair, VerifySignature


class EcdsaTest(TestCase):

    def test_sig_with_correct_parameters(self):
        bits, sig, message, pub = self.createSut()
        verifier = VerifySignature(bits, pub, sig, message)
        result = verifier.verify()
        self.assertEqual(result, True)

    def test_wrong_message_should_not_verify(self):
        bits, sig, message, pub = self.createSut()
        altered_mes = "Wrong message"
        verifier = VerifySignature(bits, pub, sig, altered_mes)
        result = verifier.verify()
        self.assertEqual(result, False)

    def test_wrong_sig_shoud_not_verify(self):
        bits, sig, message, pub = self.createSut()
        altered_sig = [131223132131, 132131231231]
        verifier = VerifySignature(bits, pub, altered_sig, message)
        result = verifier.verify()
        self.assertEqual(result, False)

    @staticmethod
    def createSut():
        bits = 192
        priv, pub = GenerateKeyPair(bits).generate_key()
        message = "ECDSA Test"
        sig = GenerateSignature(bits, [priv, pub], "ECDSA Test").generate_signature()
        return bits, sig, message, pub