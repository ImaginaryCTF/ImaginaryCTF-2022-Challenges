#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return open('flag.txt').read()

app.run('0.0.0.0', 1337)

