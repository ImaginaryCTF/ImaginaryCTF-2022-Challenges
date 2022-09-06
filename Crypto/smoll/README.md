# smoll
**Category:** Crypto
**Difficulty:** Medium
**Author:** Robin_Jadoul

## Description

Just a regular, run-of-the-mill RSA challenge, right?
Right?

## Distribution

- `smoll.ppy`
- `output.txt`

## Deploy notes

N/A

## Solution

Pollard's p - 1 algorithm, but the factor base should be shuffled to avoid always hitting the case where the gcd is `n`, as `p - 1` and `q - 1` share the same largest factor.
See `solve.sage` for an implementation.
