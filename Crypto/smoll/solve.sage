from Crypto.Util.number import long_to_bytes
import random, tqdm
with open("output.txt") as f:
    exec(f.read())

pr = []
for p in Primes():
    if p.nbits() > 20: break
    pr.append(p)
print(f"{len(pr)} primes in the factor base")

q = None
for a in range(3, 13):
    print(f"start {a = }")
    random.shuffle(pr) # Shuffle the factor base to avoid having the largest factor last
    for p in tqdm.tqdm(pr):
        for e in range(10):
            a = pow(a, p, n)
            if (g := gcd(a - 1, n)) == n:
                break
            if g != 1:
                q = ZZ(g)
                break
        if q is not None: break
    if q is not None: break

p = n // q
d = ZZ(pow(0x10001, -1, (p - 1) * (q - 1)))
print(long_to_bytes(int(pow(ct, d, n))))
