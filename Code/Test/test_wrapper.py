from WebApp.Wrappers import ecdsa

genW = ecdsa.GenerateKeysWrapper(192)

genW.serialize_key()

sigW = ecdsa.GenerateSigWrapper(192, 'public.pk', 'private.pk', 'cacat')

sigW.sig_wrapper()

verify = ecdsa.VerifySigWrapper(192, 'public.pk', 'sig.pk', 'cacat')

print(verify.verify_wrapper())



