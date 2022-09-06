#!/bin/bash

sftp -P 42022 ethan@chal.imaginaryctf.org
ssh -L 3306:127.0.0.1:3306 -p 42022 -fTN ethan@chal.imaginaryctf.org
echo 'select flag from ictf.ictf;' | mysql -u ethan -h 127.0.0.1 -p

