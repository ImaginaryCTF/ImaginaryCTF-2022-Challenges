# Living Without Expectations
**Category:** Crypto
**Difficulty:** Medium/Hard
**Author:** Robin_Jadoul

## Description

Sometimes you just gotta have some fun implementing bare hardness assumptions.

## Distribution

- `lwe.ppy`
- `output.txt`

## Deploy notes

N/A

## Solution

Insecure randomness is used to generate the errors.
We have some known plaintext, which implies that we know for a subset of the outputs that it corresponds to a "true" LWE sample:

- from the flag format
- the most significant bit of every next byte

If we'd know the values of the errors, it'd be easy to solve the challenge, as through some linear algebra, we could recover the value of `s`.
The key observation now is that we don't need to know the seeds of all "error streams" to have enough information to apply this approach.
It's enough that we have samples that are `len(seeds)` away from each other, as those we can all derive from a single seed.
A single seed doesn't yield the full matrix we need, but combining a few of those streams is still within acceptable brute force range, and gets us over the threshold.
