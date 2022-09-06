#!/usr/bin/env python3

image = open("flag.png", "rb").read().decode("latin1")
open("corrupted.png", "w").write(image)
