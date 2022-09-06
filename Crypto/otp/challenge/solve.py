from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
import re
context.log_level = 'debug'
def attempt():
#  conn = process(["python3", "./otp.py"])
  conn = remote("otp.ictf.kctf.cloud", 1337);conn.recvuntil(b"!")
  bits = [0]*800
  iter = 50
  flag = open("flag.txt", "rb").read()
  flag_len = len(flag)
  flag = bytes_to_long(flag)
  for n in range(iter):
    conn.recvuntil(b": ")
    conn.sendline(b"FLAG")
    conn.recvuntil(b": ")
    ct = long_to_bytes(int(conn.recvline(), 16))
    for i,n in enumerate(bin(bytes_to_long(ct) ^ (2**(len(ct)*8)-1))[2:]):
      if n == '1':
        bits[i] += 1
  out = ""
  for i,n in enumerate(bits):
    if n > iter//2 and i%8 != 0: # ascii character range
      out += '1'
    else:
      out += '0'
  conn.close()
  return long_to_bytes(int(out, 2))

while True:
  res = attempt()
  if b"ictf" in res:
    print(res.replace(b'\0', b""))
    break
