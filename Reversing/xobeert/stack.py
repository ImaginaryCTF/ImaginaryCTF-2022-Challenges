zero=lambda f:0
one=lambda f:1
initstack=lambda f:[]

add=lambda a:lambda b:a+b
@add
@one
class succ:pass

push=lambda x: lambda stack:[x]+stack
pop=lambda stack: stack[1:]
add=lambda stack: [stack[1]+stack[0]]+stack[2:]
sub=lambda stack: [stack[1]-stack[0]]+stack[2:]
pow=lambda stack: [stack[1]**stack[0]]+stack[2:]
mult=lambda stack: [stack[1]*stack[0]]+stack[2:]
getret=lambda stack: stack[0]

@push
@zero
class push0:pass

@push
@succ
@zero
class push1:pass

@push
@getret
@add
@push1
@push1
@initstack
class push2:pass

@push
@getret
@add
@push2
@push1
@initstack
class push3:pass

@push
@getret
@mult
@push2
@push2
@initstack
class push4:pass

@push
@getret
@add
@push2
@push3
@initstack
class push5:pass

@push
@getret
@mult
@push2
@push3
@initstack
class push6:pass

@push
@getret
@add
@push2
@push5
@initstack
class push7:pass

@push
@getret
@pow
@push3
@push2
@initstack
class push8:pass

@push
@getret
@add
@push2
@push8
@initstack
class push10:pass

@push
@getret
@add
@push4
@push7
@initstack
class push11:pass

@push
@getret
@add
@push2
@push11
@initstack
class push13:pass

@push
@getret
@mult
@push5
@push3
@initstack
class push15:pass

@push
@getret
@pow
@push4
@push2
@initstack
class push16:pass

@push
@getret
@add
@push1
@pow
@push4
@push2
@initstack
class push17:pass

@push
@getret
@mult
@push5
@push4
@initstack
class push20:pass

@push
@getret
@mult
@push3
@push7
@initstack
class push21:pass

@push
@getret
@mult
@push2
@push11
@initstack
class push22:pass

@push
@getret
@add
@push2
@push21
@initstack
class push23:pass

@push
@getret
@pow
@push5
@push2
@initstack
class push32:pass


@push
@getret
@add
@push1
@pow
@push5
@push2
@initstack
class push33:pass

@push
@getret
@add
@push1
@mult
@push5
@push8
@initstack
class push41:pass

@push
@getret
@mult
@push5
@push10
@initstack
class push50:pass

@push
@getret
@add
@push2
@mult
@push7
@push8
@initstack
class push58:pass

@push
@getret
@add
@push3
@mult
@push7
@push8
@initstack
class push59:pass

@push
@getret
@sub
@push1
@mult
@push16
@push4
@initstack
class push63:pass

@push
@getret
@add
@push1
@mult
@push16
@push4
@initstack
class push65:pass

@push
@getret
@add
@push3
@mult
@push16
@push4
@initstack
class push67:pass

@push
@getret
@mult
@push10
@push7
@initstack
class push70:pass

@push
@getret
@add
@push1
@mult
@push10
@push7
@initstack
class push71:pass

@push
@getret
@add
@push7
@mult
@push16
@push5
@initstack
class push87:pass

@push
@getret
@sub
@push2
@mult
@push3
@pow
@push5
@push2
@initstack
class push94:pass

@push
@getret
@sub
@push1
@mult
@push3
@pow
@push5
@push2
@initstack
class push95:pass

@push
@getret
@add
@push1
@mult
@push3
@pow
@push5
@push2
@initstack
class push97:pass

@push
@getret
@mult
@push2
@pow
@push2
@push7
@initstack
class push98:pass

@push
@getret
@sub
@push1
@mult
@push20
@push5
@initstack
class push99:pass

@push
@getret
@mult
@push20
@push5
@initstack
class push100:pass

@push
@getret
@add
@push1
@mult
@push5
@push20
@initstack
class push101:pass

@push
@getret
@add
@push2
@mult
@push5
@push20
@initstack
class push102:pass

@push
@getret
@add
@push3
@mult
@push5
@push20
@initstack
class push103:pass

@push
@getret
@sub
@push1
@mult
@push5
@push21
@initstack
class push104:pass

@push
@getret
@mult
@push5
@push21
@initstack
class push105:pass

@push
@getret
@add
@push3
@mult
@push5
@push21
@initstack
class push108:pass

@push
@getret
@add
@push4
@mult
@push5
@push21
@initstack
class push109:pass

@push
@getret
@mult
@push5
@push22
@initstack
class push110:pass

@push
@getret
@add
@push1
@mult
@push5
@push22
@initstack
class push111:pass

@push
@getret
@add
@push3
@mult
@push5
@push22
@initstack
class push113:pass

@push
@getret
@sub
@push1
@mult
@push5
@push23
@initstack
class push114:pass

@push
@getret
@mult
@push5
@push23
@initstack
class push115:pass

@push
@getret
@add
@push115
@push1
@initstack
class push116:pass

@push
@getret
@add
@push115
@push3
@initstack
class push118:pass

@push
@getret
@sub
@push1
@mult
@push11
@push11
@initstack
class push120:pass

@push
@getret
@mult
@push11
@push11
@initstack
class push121:pass

@push
@getret
@add
@push2
@mult
@push11
@push11
@initstack
class push123:pass

@push
@getret
@add
@push1
@mult
@push4
@mult
@push3
@push11
@initstack
class push133:pass

@push
@getret
@add
@push5
@mult
@push4
@mult
@push3
@push11
@initstack
class push137:pass

@push
@getret
@sub
@mult
@push3
@push3
@mult
@push13
@push13
@initstack
class push160:pass

@push
@getret
@mult
@push13
@push13
@initstack
class push169:pass

@push
@getret
@mult
@push7
@mult
@push5
@push5
@initstack
class push175:pass

@push
@getret
@add
@push1
@mult
@push16
@push11
@initstack
class push177:pass

@push
@getret
@add
@push8
@mult
@push16
@push11
@initstack
class push184:pass

@push
@getret
@mult
@push15
@push13
@initstack
class push195:pass

@push
@getret
@add
@push10
@mult
@push15
@push13
@initstack
class push205:pass

@push
@getret
@add
@push1
@mult
@mult
@push3
@push3
@mult
@push5
@push5
@initstack
class push226:pass

@push
@getret
@sub
@push1
@mult
@push2
@pow
@push3
@push5
@initstack
class push249:pass

@push
@getret
@mult
@push2
@pow
@push3
@push5
@initstack
class push250:pass

@push
@getret
@add
@push1
@push250
@initstack
class push251:pass

@__import__
@bytes.decode
@bytes
@push115
@push121
@push115
@initstack
class sys:pass

@__import__
@bytes.decode
@bytes
@push114
@push97
@push110
@push100
@push111
@push109
@initstack
class random:pass

@sys.__dict__.get
@bytes.decode
@bytes
@push101
@push120
@push105
@push116
@initstack
class exit:pass

@random.__dict__.get
@bytes.decode
@bytes
@push115
@push101
@push101
@push100
@initstack
class seed:pass

@random.__dict__.get
@bytes.decode
@bytes
@push114
@push97
@push110
@push100
@push98
@push121
@push116
@push101
@push115
@initstack
class randbytes:pass


@input
@bytes.decode
@bytes
@push102
@push108
@push97
@push103
@push63
@push32
@initstack
class userinput:pass
ui=lambda _:userinput

@len
@ui
class inputlen:pass
il=lambda _:inputlen

@range
@il
class r:pass

otp=lambda x:lambda y:[x[i]^y[i] for i in r]

@otp
@str.encode
@ui
class otp:pass

const=lambda x:lambda _:x

@const
@bytes.decode
@bytes
@push87
@push114
@push111
@push110
@push103
@push33
@initstack
class wrong:pass


@const
@bytes.decode
@bytes
@push67
@push111
@push114
@push114
@push101
@push99
@push116
@push32
@push58
@push41
@initstack
class correct:pass

# [123, 250, 94, 95, 121, 195, 249, 70, 71, 59, 137, 59, 5, 67, 65, 226, 17, 160, 205, 100, 251, 169, 50, 118, 184, 177, 1, 175, 133]
# for flag: ictf{wh0_n33d5_c4ll5_4nyw4y?}

@const
@push133
@push175
@push1
@push177
@push184
@push118
@push50
@push169
@push251
@push100
@push205
@push160
@push17
@push226
@push65
@push67
@push5
@push59
@push137
@push59
@push71
@push70
@push249
@push195
@push121
@push95
@push94
@push250
@push123
@initstack
class check:pass

@list.reverse
@check
class xx:pass

@check
class check:pass

x=lambda f:lambda x: [wrong, correct][x == check]
@x
class checkflag:pass

@checkflag
@otp
@randbytes
@il
@seed
@randbytes
@il
@seed
@bytes.decode
@bytes
@push100
@push101
@push98
@push100
@push98
@push101
@push101
@push102
@push95
@push111
@push114
@push95
@push115
@push116
@push104
@initstack
class read:pass

@print
@read
class main:pass

