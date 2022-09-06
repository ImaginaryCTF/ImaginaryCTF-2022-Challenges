from pwn import *

#conn = process(["python3", "./neoannophobia.py"])
conn = remote("neoannophobia.ictf.kctf.cloud", 1337)

#context.log_level = 'debug'

winning = [[n,19+n] for n in range(1,13)]
# If you stay on these numbers, you can force your opponent onto November 30, and then to December 31.

def n2d(date: list):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return f"{months[date[0]-1]} {date[1]}"

def d2n(date: str):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
    try:
        out = [months.index(date.split()[0])+1, int(date.split()[1])]
    except:
        conn.interactive()
    return out

# This is a "good enough" solution. If the computer (by chance) does the
# winning strategy (or as a result of the "smarter" computer in later games),
# this will fail. A perfect solution is impossible becuase in this game, you
# do not play first.
for _ in range(1, 101):
    conn.recvuntil("----------\n")
    conn.recvuntil("----------\n")
    won = False
    while not won:
        r = d2n(conn.recvline().strip().decode())
        conn.recvuntil("> ")
        if r in winning:
            conn.sendline(n2d([r[0],r[1]+1]))
        if r[1] < 20:
            conn.sendline(n2d([1,20]))
        else:
            for d in winning[1:]:
                if (d[1] == r[1] or d[0] == r[0]) and (d[0] > r[0] or (d[0] == r[0] and d[1] > r[1])):
                    conn.sendline(n2d(d))
                    if d == [12,31]:
                        won = True
    print(f"{_} is won!")

conn.recvline()
print(conn.recvline().strip().decode())
