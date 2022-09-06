# polymorphic
**Category:** Reversing
**Difficulty:** Medium
**Author:** TheBadGod

## Description

Name says it all. Don't crash!

## Distribution

- `polymorphic`

## Deploy notes

None

## Solution

use gdb to run until the next byte get's checked. Or using static analysis do the xor's by hand. Will probably do a script tomorrow or so. But looking at ghidra also reveals the code, because ghidra/binja computes the result of the xor already, because it's not dynamically calculated. But they also contain some wrong instructions (But I made sure that all instructions are actually valid)
