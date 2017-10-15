from hashlib import sha256
import string #'string' module used for getting all printable letters (chars)
def foo(N,K) :
	import binascii
	fmt = '%%0%dx' % N
	bits = binascii.unhexlify(fmt % K)
	return (bits)

for k in xrange(0,10000):
    bb = foo(10,k)
    hh = sha256(bb)
    print hh
exit()    
xstr = lambda s: s or ''
spindex = [0]
spstring = ''
chars = [None]
for item in range(0, len(string.printable)):
	chars.append(string.printable[item])
targethash = 'e37a649e5b4e9dd25672f22470f7ac0e5a902c2e02b54f9adc8ce791383d7514' #sha256 of what produces this hash?
while True: #forever, untill program is killed when it finds correct sha256 input
	hashed = sha256(spstring.rstrip()).hexdigest()#produce a new hash to check
	
	if hashed == targethash: # check hash
	    print('"' + spstring.rstrip().decode()+ '" ' + 'completes the block!')
	    exit(1) #exit program if correct sha256 input is found
	spindex[0] += 1 #increment sha256 input
	spstring = '' #clear spstring
	for item in range(0, len(spindex)): #rollover
		if spindex[item] == 101:
			print "trying: " + spstring
			spindex.append(0)
			spindex[item+1] += 1
			spindex[item] = 0
		spstring += xstr(chars[spindex[item]])


def foo(N,K) :
	import binascii
	fmt = '%%0%dx' N
	bits = binascii.unhexlify(fmt % K)
	print (bits)