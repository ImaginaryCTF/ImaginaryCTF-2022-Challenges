#!/usr/bin/env python3
import random

intro = '''Welcome to neoannophobia, where we are so scared of New Year's that we race to New Year's eve!

In this game, two players take turns saying days of the year ("January 30", "July 5", etc)

The first player may start with any day in the month of January, and on each turn a player may say another date that either has the same month or the same day as the previous date. You can also only progress forward in time, never backwards.

For example, this is a valid series of moves:

Player 1: January 1
Player 2: February 1
Player 1: February 9
Player 2: July 9
Player 1: July 14
Player 2: July 30
Player 1: December 30
Player 2: December 31

This is an illegal set of moves:

Player 1: January 1
Player 2: July 29 (not same day or month)
Player 1: July 1 (going backwards in time)

The objective of the game is simple: be the first player to say December 31.

The computer will choose its own moves, and will always go first. To get the flag, you must win against the computer 100 times in a row.

Ready? You may begin.

'''

current_date = [1,1]

def n2d(date: list):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return f"{months[date[0]-1]} {date[1]}"

def d2n(date: str):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
    out = [months.index(date.split()[0])+1, int(date.split()[1])]
    assert out[1] <= lengths[out[0]-1] and out[1] > 0
    assert out[0] >= current_date[0] and out[1] >= current_date[1]
    assert out[0] == current_date[0] or out[1] == current_date[1]
    assert out != current_date
    return out

def gen(f=False, i=0):
    if f:
        return [1,random.randint(1,31)]
    if bool(current_date[0] == 12) != bool(current_date[1] == 31):
        return [12,31]
    if bool(current_date[0] == 11) != bool(current_date[1] == 30):
        return [11,30]
    if i > 30:
        if bool(current_date[0] == 10) != bool(current_date[1] == 29):
            return [10,29]
        if bool(current_date[0] == 9) != bool(current_date[1] == 28):
            return [9,28]
        if bool(current_date[0] == 8) != bool(current_date[1] == 27):
            return [8,27]
    if i > 65:
        if bool(current_date[0] == 7) != bool(current_date[1] == 26):
            return [7,26]
        if bool(current_date[0] == 6) != bool(current_date[1] == 25):
            return [6,25]
        if bool(current_date[0] == 5) != bool(current_date[1] == 24):
            return [5,24]
        if bool(current_date[0] == 4) != bool(current_date[1] == 23):
            return [4,23]
    lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
    c = random.randint(0,1)
    if current_date == [11,30]:
        return [12,30] if c else [11,31]
    if c==1:
        out = [random.randint(current_date[0]+1, 11), current_date[1]]
    elif c==0:
        out = [current_date[0], random.randint(current_date[1]+1, lengths[current_date[0]-1])]
    return out

print(intro)
for _ in range(1,101):
    print("----------")
    print(f"ROUND {_}")
    print("----------")

    w = "c"
    current_date = gen(f=True)
    print(n2d(current_date))
    while current_date != [12,31]:
        current_date = d2n(input("> "))
        if current_date == [12,31]:
            w = "p"
            break
        current_date = gen(f=False, i=_)
        print(n2d(current_date))
        if current_date == [12,31]:
            w = "c"
            break
    if w == "c":
        print("You lost. Better luck next time.")
        exit()
    else:
        print("You won!")

print(open("flag.txt").read())
