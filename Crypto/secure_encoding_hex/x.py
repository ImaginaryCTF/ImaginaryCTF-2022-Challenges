#!/usr/bin/env python3

from itertools import permutations

ct = '0d0b18001e060d090d1802131dcf011302080ccf0c070b0f080d0701cf00181116'

translate = {
    '0': '6',
    'd': '9',
    'b': '3',
    '1': '7',
    '8': '4',
    'e': 'b',
    '6': 'd',
    # above from knowing `ictf{}`
    'c': '5',
    'f': 'f',
    # above from noticing underscores
}

unused_ct = '234579a'
unused_pt = '12680ac'

for s in permutations(unused_ct):
    d = {**translate, **{s[i]:c for(i,c) in enumerate(unused_pt)}}
    out = bytes.fromhex(''.join(d[i] for i in ct))
    if len(str(out)) == 36:
        print(out)