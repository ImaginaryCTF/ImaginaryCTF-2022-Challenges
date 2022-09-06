# xobeert
**Category:** Reversing
**Difficulty:** Medium
**Author:** TheBadGod

## Description

My friend played GoogleCTF. Afterwards they sent me
this AST of their solution to one of the challenges.

Apparently it also checks for a flag? Please help me
find their hidden flag!

Also it looks like you need python 3.9 or later!

## Distribution

- `ast.txt`

## Deploy notes

None

## Solution

It's a simple ast, but the decorator_list are important, there
are no function calls, but the decorators are called with the
output of the previous decorator's output (or the function /
class the decorators are part of)

See the actual source in stack.py

We can reverse the push calls to get the numbers, then we can
reverse the second to last class, which pushes a few values to
the stack and then calls another function we defined as well
as the check value, important here the size of it.

The solution is to replicate the whole setup:

```
seed("debdbeef_or_sth")
seed(randbytes(len(check)))
bytes([a^b for a,b in zip(check, randbytes(len(check)))])
```
