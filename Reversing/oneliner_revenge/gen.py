#!/usr/bin/env python3

from random import randint

a = b"ictf{0n3l1n3is5uperior!}"

def gen_condition(t):
    lhs = '+'.join(str(randint(1,99))+'*a[%d]'%randint(0,len(a)-1) for i in range(5))
    rhs = '+'.join(str(randint(1,99))+'*a[%d]'%randint(0,len(a)-1) for i in range(5))
    diff = eval(lhs)-eval(rhs)
    if not t:
        diff += randint(1,10)
    return (lhs+'=='+rhs+'+%d'%diff).replace('+-','-')

def gen_lambda(n):
    return "lambda*a:(%s)"%','.join(gen_condition(i=='1') for i in "{:04b}".format(n))

num = 1
conds = []
for i in range(16):
    conds.append(gen_lambda(num))
    num += 1
    num %= 16

out = []
for cond in conds[::-1]:
    out = [cond] + out
    out.reverse()

print(',\n'.join(out))