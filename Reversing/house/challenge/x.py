#!/usr/bin/env python3

from pwn import *
from z3 import *


nums = []

def add_fake():
    if len(nums) < 31 or nums[-3] == -1 or nums[-31] == -1:
        nums.append(-1)
    else:
        nums.append((nums[-3]+nums[-31])%65536)

def gamble_safe(p):
    p.recvuntil('>>> ')
    p.sendline('5')
    num = int(p.recvline().strip().decode().split()[-1][:-1])
    add_fake()
    nums.append(num)
    p.recvuntil('>>> ')
    if num < 32768:
        p.sendline('1')
    else:
        p.sendline('2')
    num = int(p.recvline().strip().decode().split()[-1][:-1])
    add_fake()
    nums.append(num)

def gamble_risky(p):
    p.recvuntil("money: ")
    money = int(p.recvline().strip().decode())
    print("current money", money)
    if money > 1000_000_000:
        p.interactive()
    p.recvuntil('>>> ')
    p.sendline(str(money))
    num = int(p.recvline().strip().decode().split()[-1][:-1])
    add_fake()
    nums.append(num)
    predicted = (nums[-2] + nums[-30])%65536
    p.recvuntil('>>> ')
    if num < predicted:
        p.sendline('1')
    else:
        p.sendline('2')
    num = int(p.recvline().strip().decode().split()[-1][:-1])
    add_fake()
    nums.append(num)


#p = process(["./casino"])
p = remote("the-house-always-wins.ictf.kctf.cloud", 1337)
#context.log_level = 'debug'

for i in range(32):
    gamble_safe(p)

print("Read nums:", nums)

while True:
    gamble_risky(p)

for i in range(20):
    next_num = (nums[-2] + nums[-30]) % 65536
    p.recvuntil('>>> ')
    p.sendline('5')
    num = int(p.recvline().strip().decode().split()[-1][:-1])
    add_fake()
    nums.append(num)
    print("Predicted:", next_num, "Actual:", num)
    next_num = (nums[-2] + nums[-30]) % 65536
    p.recvuntil('>>> ')
    p.sendline('1')
    num = int(p.recvline().strip().decode().split()[-1][:-1])
    add_fake()
    nums.append(num)
    print("Predicted:", next_num, "Actual:", num)

