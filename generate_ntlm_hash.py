import hashlib
import binascii
import sys 

# One-liner form: python -c 'import hashlib,binascii; print binascii.hexlify(hashlib.new("md4", "<password>".encode("utf-16le")).digest())'

# Check if a password was sent
arguments = len(sys.argv)
if arguments == 1:
    print "Usage: " + sys.argv[0] + " password"
    exit()

# Calculate and return the hash
pass1 = sys.argv[1]
hash1 = binascii.hexlify(hashlib.new("md4", pass1.encode("utf-16le")).digest())
print pass1, hash1
