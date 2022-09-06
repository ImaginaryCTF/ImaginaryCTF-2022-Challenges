from string import printable
printable = printable.encode()

content = [b for b in open("corrupted.png", "rb").read()]
out = []

while content != []:
  b = content.pop(0)
  if b in (0xc2,0xc3) and content[0] not in printable:
    if b == 0xc3:
      out.append(content.pop(0) + 64)
    if b == 0xc2:
      out.append(content.pop(0))
  else:
    out.append(b)

open("out.png", "wb").write(bytes(out))
