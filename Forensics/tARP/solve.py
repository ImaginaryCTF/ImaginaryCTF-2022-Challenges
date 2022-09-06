import os
import re

data = os.popen("tshark -r tarp.pcapng -Y arp -T fields -e arp.dst.proto_ipv4 | grep -v 10.42.10.").read()
data = [int(n) for n in data.replace("\n", " ").replace(".", " ").split()]
print(bytes(data))
while data[0] != 0x89: # PNG header
  data.pop(0)

open("out.png", "wb").write(bytes(data))


