from z3 import * # I like to pretend that I know crypto, please forgive my inability to use z3 either
from pwn import *

config = [[int(a) for a in n.strip()] for n in open("jbox.txt").readlines()] # sbox pbox jack in the box

def sha42(s: bytes, rounds=42):
  out = [0]*21
  for round in range(rounds):
    for c in range(len(s)):
      if config[((c//21)+round)%len(config)][c%21] == 1:
        out[(c+round)%21] ^= s[c]
  return bytes(out).hex()

def collide(hash):
  target = [n for n in bytes.fromhex(hash)]
  a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20 = BitVecs(" ".join([f"a{n}" for n in range(21)]), 8)
  s = Solver()
  for j in range(21):
    out = "s.add("
    for i in range(21):
      if sha42(b'\0'*i + b"\xff" + b'\0'*(21-i-1)).replace('ff', '1').replace('00', '0')[j] == '1':
        out += f"a{i}^"
    out = out[:-1]
    out += f" == {target[j]})"
    exec(out) # yikes
  s.check()
  a = bytes([int(str(s.model()[n])) for n in [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20]])
  assert sha42(a) == hash
  return a

#conn = process(["python3", "./chal.py"])
conn = remote("hash.ictf.kctf.cloud", 1337); conn.recvline()
#context.log_level = 'debug'
for n in range(50):
  conn.recvuntil(b"= ")
  hash = conn.recvline().strip().decode()
  conn.recvuntil(b"= ")
  c = collide(hash).hex()
  info(f"hash(unhex({c})) = {hash}")
  conn.sendline(c.encode())

conn.recvuntil(b"flag is: ")
print(conn.recvline())
