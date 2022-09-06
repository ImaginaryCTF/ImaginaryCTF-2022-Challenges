#!/usr/bin/env python3

from flask import Flask, render_template_string, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/ssti')
def ssti():
    query = request.args['query'] if 'query' in request.args else '...'
    if len(query) > 48:
        return "Too long!"
    return render_template_string(query)

app.run('0.0.0.0', 1337)
