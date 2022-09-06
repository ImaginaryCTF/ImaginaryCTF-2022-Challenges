#!/usr/bin/env python3

while True:
  a = input(">>> ")
  assert all(n in "()abcdefghijklmnopqrstuvwxyz" for n in a)
  exec(a)
