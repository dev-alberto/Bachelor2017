from util import isProbablePrime


primes_under_1000 = [i for i in range(2, 1000) if isProbablePrime(i)]

assert len(primes_under_1000) == 168

number = 643808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153

assert isProbablePrime(number) is True
