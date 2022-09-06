# gdb -q -x solve.py

import gdb
import string
import re

flag = "ictf"

while not "}" in flag:
  gdb.execute("file ./polymorphic")
  gdb.execute(f"r <<<$(echo {flag}\x90)") # this character will never be in the flag
  bad = int(gdb.execute("p (int)$_siginfo._sifields._sigfault.si_addr", to_string=True).split()[-1], 0)%2**(8*3)
  for c in [n for n in string.printable if not n in '\' \t\n"']:
    gdb.execute("file ./polymorphic")
    gdb.execute(f"r <<<$(echo '{flag+c}')")
    try:
      addr = int(gdb.execute("p (int)$_siginfo._sifields._sigfault.si_addr", to_string=True).split()[-1], 0)%2**(8*3)
      if addr != bad:
        flag += c
        print(flag)
        break
    except:
      flag += c
      print(flag)
