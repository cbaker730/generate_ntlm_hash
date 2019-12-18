#!/usr/bin/env python3


__author__ = 'Chris Baker (@bakerc)'
__date__ = '20191218'
__version__ = '0.01'
__description__ = """Determine the NTLM hash for a given password"""


import argparse
import os
import hashlib
import binascii
import sys


def main():

    # Calculate and return the hash
    hash_pass = binascii.hexlify(hashlib.new("md4", cleartext_pass.encode("utf-16le")).digest())
    output = cleartext_pass + ' ' + hash_pass.decode()

    if args.outfile:
        print("[*] Writing to {}...".format(args.outfile))
        output += '\n'
        with open(args.outfile, 'w', encoding="utf8", errors='ignore') as fh:
            fh.write(output)
    else:
        print(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--password", help="Specify the password to be hashed.")
    parser.add_argument("-o", "--outfile",  help="Writes the output to the specified file.")
    args = parser.parse_args()

    if args.password:
        cleartext_pass = args.password
    else:
        cleartext_pass = 'samantha05'

    main()
