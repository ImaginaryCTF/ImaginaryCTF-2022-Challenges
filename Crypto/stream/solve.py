from pwn import u64, p64
from string import printable
import os

p = printable.encode()
ct = open("out.txt", "rb").read()

for ku in range(2**24):
  key = u64(ct[0:8]) ^ (u64(b'ictf{\0\0\0') + ku*16**10)
  if pow(key, 32, 2**64)>>40 == 0x2297b4:
    os.system(f"./stream out.txt {key} tmp; cat tmp; rm tmp")
