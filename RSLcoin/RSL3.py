from hashlib import sha256
import string #'string' module used for getting all printable letters (chars)
def foo(N,K) :
	import binascii
	fmt = "%%0%dx" % N
	bits = binascii.unhexlify(fmt % K)
	return (bits)

for k in xrange(0,10000):
    bb = foo(10,k)
    hh = sha256(bb).hexdigest()
    print hh
