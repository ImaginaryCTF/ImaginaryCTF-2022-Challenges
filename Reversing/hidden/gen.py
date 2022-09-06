from pwn import *
import binascii
import os

context.binary = elf = ELF("./hidden_orig")
sc = "31 C0 31 FF 48 83 EC 1E 48 89 E6 BA 1E 00 00 00 0F 05 49 89 F2 49 BE 08 EB 3D F8 FD 96 0A 91 41 56 49 BE 55 5B 49 31 93 9C 5E 43 41 56 49 BE F9 D6 99 F4 8B 14 70 78 41 56 49 89 E3 49 C7 C7 00 00 00 00 49 B8 94 3C 57 2F B3 24 E3 39 4D 0F AF C0 4D 33 02 49 BD 66 61 69 6C 21 0A 00 00 41 55 48 89 E6 4D 3B 03 75 1F 49 FF C7 49 83 FF 03 74 0A 49 83 C2 08 49 83 C3 08 EB D2 49 BD 63 6F 72 72 65 63 74 0A 41 55 48 89 E6 31 C0 FF C0 31 FF FF C7 BA 08 00 00 00 0F 05 31 C0 83 C0 3C 0F 05".replace(" ", "").replace("\n", "")
sc = binascii.unhexlify(sc)
print(sc)
print(len(sc))

elf.write(elf.plt.puts-4, sc)
elf.save("hidden")
os.system("chmod +x hidden")
