#!/usr/bin/env python3

from base64 import b64encode, b64decode
from collections import Counter

word_len = 4
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/='

def common(lst):
    return max(lst, key=Counter(lst).get)

text =open("wilde.txt", "r").read()
ct = open("out.txt", "r").read()
while '  ' in text:
    text = text.replace('  ', ' ')
while '\n\n\n' in text:
    text = text.replace('\n\n\n', '\n\n')
text = b64encode(text.encode()).decode()

while '  ' in ct:
    ct = ct.replace('  ', ' ')
while '\n\n\n' in ct:
    ct = ct.replace('\n\n\n', '\n\n')
ct_save = ct
freqs = [{} for i in range(word_len)]
ct_freqs = [{} for i in range(word_len)]


while len(text) > 0:
    word = text[:word_len]
    text = text[word_len:]
    for i, char in enumerate(word):
        if char not in freqs[i]:
            freqs[i][char] = 0
        freqs[i][char] += 1

while len(ct) > 0:
    word = ct[:word_len]
    ct = ct[word_len:]
    for i, char in enumerate(word):
        if char not in ct_freqs[i]:
            ct_freqs[i][char] = 0
        ct_freqs[i][char] += 1

for j in range(word_len):
    freqs[j] = sorted(((i,freqs[j][i]) for i in freqs[j]), key=lambda x:x[1], reverse=True)
    ct_freqs[j] = sorted(((i,ct_freqs[j][i]) for i in ct_freqs[j]), key=lambda x:x[1], reverse=True)

print(freqs)
print(ct_freqs)

pairings = []

for i in range(word_len):
    print(len(freqs[i]))
    print(len(ct_freqs[i]))
    pairings.append({v[0]:freqs[i][j][0] for(j,v)in enumerate(ct_freqs[i]) if j<len(ct_freqs[i]) and j < len(freqs[i])})

print(pairings)

translate = {}

for d in pairings:
    new_d = {}
    for i, c in enumerate(d):
        new_d[i] = d[c]
    d.update(new_d)

for d in pairings:
    for i, c in enumerate(d):
        if c not in translate:
            translate[c] = []
        translate[c].append(d[c])
        if i != 0:
            translate[c].append(d[i-1])
        if i != len(d):
            try:
                translate[c].append(d[i+1])
            except KeyError:
                break

print(translate)

possible = {c:common(translate[c]) for c in translate}

print()
print(possible)

pt = ''.join(possible[c] for c in ct_save)

print(''.join(chr(i) for i in b64decode(pt.encode())))
