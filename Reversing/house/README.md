# The House Always Wins
**Category:** Reversing
**Difficulty:** Medium
**Author:** puzzler7

## Description

They say that the house always wins - come find out if that's actually true.

## Distribution

- `casino`
- netcat link

## Deploy notes

Simply host `casino` on a port.

## Solution

See `x.py` for a solve script.

The casino uses glibc randomness - although it's seeded securely, and the player only gets the high 16 bits of each number, because each number is the sum of two previous ones, the player can predict the future numbers after extracting several of them. 

See [https://www.mathstat.dal.ca/~selinger/random/](https://www.mathstat.dal.ca/~selinger/random/) for a description of the implementation of the rand function.
