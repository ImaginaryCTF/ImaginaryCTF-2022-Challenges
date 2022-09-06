# One Liner: Revenge
**Category:** Reversing
**Difficulty:** Medium/Hard
**Author:** puzzler7

## Description

The last time that I made a python one-liner challenge, I recieved two pieces of feedback. First, it's not a meaningful one-line challenge if the player can just ... add new lines. Second, "walrus operators are cringe". I've taken both of these criticisms to heart. Have fun!

## Distribution

- revenge.py

## Deploy notes

n/a

## Solution

The file compares the flag against many different conditions, some of which must be true, some of which must be false. The player can determine which these are by replacing the existing lambdas with lambdas that return a tuple of 4 bits, and adding a print statement to see how far in the list of conditions the checker gets. From there, simply plugging the conditions into z3 yields the flag. See `x.py` for a solve script.
