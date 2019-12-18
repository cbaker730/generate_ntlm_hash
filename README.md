# Generate NTLM hash

generate_ntlm_hash.py is a python script that calculates an NTLM hash from a known password

Usage: python generate_ntlm_hash.py samantha05

```
root@kali:~# python generate_ntlm_hash.py samantha05
samantha05 eac9f53ac5b060f0b91ce355a88be845
```

Or, in Python3:

```
root@kali:~# python3 generate_ntlm_hash_python3.py -p samantha05
samantha05 eac9f53ac5b060f0b91ce355a88be845

root@kali:~# python3 generate_ntlm_hash_python3.py -p samantha05 -o hashfile.txt
[*] Writing to hashfile.txt...
root@kali:~# cat hashfile.txt 
samantha05 eac9f53ac5b060f0b91ce355a88be845
```
