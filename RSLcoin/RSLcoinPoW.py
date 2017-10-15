from hashlib import sha256, md5
import time
import sys
import binascii
difficulty = 6

test = '0' * difficulty
print
fmt = "%%0%dx" % 24 #will format as hexadecimal, with size 4 bytes
i=0
for k in xrange(0,10000000000):
    bits = binascii.unhexlify(fmt % k)
    # could also use .decode('hex')  even better in python 3 every integer has a to_bytes function!!!

    nhash = md5(bits).hexdigest() #generate new hash to try
    #print k, nhash[0:8]
    if test == nhash[0:difficulty]:
    	i+=1
    	if ( i%15 ) ==0:
    		print "\033[16A"
    	print "\033[K",' ',i,k, nhash, fmt %k,chr(13)
    	#print "\033[K",
    	#sys.stdout.flush()