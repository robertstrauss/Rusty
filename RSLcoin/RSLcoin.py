from hashlib import sha256, md5
import time
import binascii
fmt = "%%0%dx" % 8 #will format as hexadecimal, with size 4 bytes
for k in xrange(0,10000000000):
    bits = binascii.unhexlify(fmt % k)
    nhash = md5(bits).hexdigest() #generate new hash to try
    #print k, nhash[0:8]
    if '00000' == nhash[0:5]:
    	print k, nhash