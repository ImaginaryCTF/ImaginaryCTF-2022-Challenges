output = [int(i[::-1],2) ^ 0b10011010 for i in open("out.txt").readlines()] # transcribed from video

def deobfuscate(l, seed):
  out = []
  for n in l:
    out.append(n ^ (seed % 256))
    lsb = seed & 1
    seed >>= 1
    if lsb == 1:
      seed ^= 0xAD00
  return out

print(bytes(deobfuscate(output, ord('i')^output[0])))
