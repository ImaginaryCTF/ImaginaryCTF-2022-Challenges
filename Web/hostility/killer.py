#!/usr/bin/env python3

from time import sleep
from os import system

while 1:
    print('before docker call')
    system('docker-compose down && docker-compose up --build -d')
    print("after system call")
    sleep(300)
    print('after sleep')
