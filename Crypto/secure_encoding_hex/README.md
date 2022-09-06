# Secure Encoding: Hex
**Category:** Crypto
**Difficulty:** Easy
**Author:** puzzler7

## Description

Cryptograms == encryption, right? Flag is readable english.

## Distribution

- encode.py
- out.txt

## Deploy notes

n/a

## Solution

The hex characters have been shuffled around. By noting that the first few characters are `ictf{` and the last character is `}`, you can solve 7 of 16 shuffled characters. Additionally, 3 of the characters have a different starting digit - you can infer that these are underscores, solving 9 of 16. The rest of the digits can be brute forced.

(There are definitely ways to solve without guessing the underscores, but I'm just lazy)
