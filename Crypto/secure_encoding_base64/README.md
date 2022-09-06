# Secure Encoding: Base64
**Category:** Crypto
**Difficulty:** Medium
**Author:** puzzler7

## Description

Base64 is my favorite encryption scheme.

## Distribution

- encode.py
- out.txt

## Deploy notes

n/a

## Solution

We can perform a frequency analysis on every fourth character, comparing to another large body of text. The solve script `x.py` here does so, and yields a translation good enough to realize that the plaintext is The Picture of Dorian Gray, from Project Gutenberg. From there, the translation can be refined.
