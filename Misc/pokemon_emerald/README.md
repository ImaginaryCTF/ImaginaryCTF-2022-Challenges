# pokemon emerald
**Category:** Misc
**Difficulty:** Easy
**Author:** Robin_Jadoul

## Description

Pyjails are getting so much attention, can you find the glitch in my video game instead?

## Distribution

- `jail.rb`
- nc connection

## Deploy notes

Run `jail.rb` with flag.txt.
The `stdbuf` in the shebang should hopefully be enough to ensure the exploit works out in the end.

## Solution

We can execute limited shell commands with `%x{}`.
From there, we can pivot to `%x{ruby}` to execute less restricted code.
You might have to fiddle a bit to get the final output back properly on the socket, since if you use netcat, it might exit before the flag is sent back.
You can either get a proper EOF through pwntools (see `solve.py`, the sleep is needed, possibly to give the buffering some time, or the second ruby process to start), or by dumping it from tcpdump (it's still sent, there's just nothing to receive it anymore).

