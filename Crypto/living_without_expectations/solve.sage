import itertools, collections, tqdm

proof.all(False)

with open("output.txt") as f:
    samples = [(list(map(eval, eval(x + "]"))), list(map(eval, eval(y)))) for line in f.read().splitlines() for (x, y) in [line.split("] ")]]

flaglen = len(samples) // 8
def isknown(index):
    index %= flaglen * 8
    if index % 8 == 0:
        return True
    return index // 8 in [flaglen - 1, 0, 1, 2, 3, 4] and f'{(b"ictf{" + bytes([0xff]) * (flaglen - 5) + b"}")[index // 8]:08b}'[index % 8] == '0'

q = 2^142 + 217
F = GF(q)
n = 69
nseeds = 142
m = sum(isknown(i) for i in range(flaglen * 8))
n_M = n + nseeds + m

def rand(seed):
    seeds = [(seed >> (3 * i)) & 7 for i in range(nseeds)]
    a = 5
    b = 7
    while True:
        for i in range(nseeds):
            seeds[i] = (a * seeds[i] + b) & 7
            yield seeds[i]


def analyze_streams():
    c = collections.Counter()
    e = itertools.cycle(range(nseeds))
    for i in range(len(samples)):
        if isknown(i):
            for _ in range(n):
                c[next(e)] += 1
    print(c)
    print(sum(x for _, x in c.most_common(3)))
# analyze_streams()

for seed in tqdm.trange(2^9):
    rng = rand(seed)
    E = itertools.cycle(range(nseeds))
    M = [] # M * s = v
    v = []
    for i, (AA, bb) in enumerate(samples):
        AA = iter(AA)
        AA = [[next(AA) for _ in range(n)] for _ in range(n)]
        for A, b in zip(AA, bb):
            ei = next(E)
            e = next(rng)
            if isknown(i) and ei < 3:
                M.append(A)
                v.append(b - e)
    try:
        s = Matrix(F, M).solve_right(vector(F, v))
        print(s)
        break
    except ValueError as err:
        if "no solution" not in err.args[0]:
            raise

s = vector(F, s)
res = []
for AA, bb in samples:
    AA = iter(AA)
    AA = [[next(AA) for _ in range(n)] for _ in range(n)]
    m = max(vector(F, bb) - Matrix(F, AA) * s)
    if m > 7:
        res.append("1")
    else:
        res.append("0")
print(int(''.join(res), 2).to_bytes(42, "big"))
