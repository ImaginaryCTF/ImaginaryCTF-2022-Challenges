#!/usr/bin/env python3

from user_backend import *

from flask import Flask, request, make_response, redirect, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from sqlite3 import *
from os import _exit
from threading import Thread
from datetime import datetime, timedelta
from time import sleep


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10000 per hour"]
)

winners = []
voting_ended = False
now = datetime.now()
vote_end_time = now + timedelta(minutes=10)
kill_time = vote_end_time + timedelta(minutes=2)

class Restart(Thread):
    def run(self):
        global voting_ended, winners
        sleep(600)
        print("setting winners")
        voting_ended = True
        votes, num_winners = get_votes()
        winners = [i[1] for i in votes[:num_winners]]
        sleep(120)
        print("killing")
        _exit(0) # killing the server, and docker should restart it

Restart().start()

'''
countdown to vote end (would be nice)
kill after 10 mins and tally winners
'''

def cast_vote(vote):
    voter_id = get_current_id(request)
    if voter_id is None:
        return "Not logged in!"
    if voting_ended:
        return "Voting has ended! Try again in a few minutes."
    if check_id_exists(vote) is None:
        return "The user you're voting for doesn't exist!"
    conn, cur = get_sql()
    ip = get_remote_address()
    cur.execute("select * from votes where ip_addr = ?", (ip,))
    existing_vote = cur.fetchone()
    # if existing_vote is not None and voter_id != existing_vote[0]:
    #     return "Someone else from that IP has already voted!"
    cur.execute("insert into votes values (?, ?, ?)", (voter_id, ip, vote))
    conn.commit()
    cur.close()
    conn.close()
    return f"Successfully voted for {vote}"

def num_votes(uid):
    conn, cur = get_sql()
    cur.execute("select * from votes where vote = ?", (uid,))
    rows = cur.fetchall()
    ret = len(rows)
    cur.close()
    conn.close()
    return ret

def get_votes():
    votes = []
    conn, cur = get_sql()
    cur.execute("select username, user_id from users")
    all_users = cur.fetchall()
    num_winners = min(len(all_users)//100 + 1, 50)
    for user in all_users:
        user_votes = num_votes(user[1])
        if user_votes > 0:
            votes.append((*user, user_votes))
    votes = sorted(votes, key=lambda x: x[2], reverse=True)
    return votes, num_winners


@limiter.limit("5/second")
@app.route('/')
def index():
    curr_user = get_current_user(request)
    votes, num_winners = get_votes()
    cd_time = kill_time if voting_ended else vote_end_time
    return render_template("index.html", user=curr_user, num_winners=num_winners, votes=votes,
                           voting_ended=voting_ended, datestr=cd_time.strftime("%m/%d/%Y, %H:%M:%S")
    )

@limiter.limit("5/second")
@app.route('/login', methods=['GET'])
def login_endpoint():
    return render_template("login.html")

@limiter.limit("5/second")
@app.route('/login', methods=['POST'])
def login_endpoint_post():
    user = request.form['user']
    pwd = request.form['pass']
    cookie = login(user, pwd)
    resp = redirect('/me', 302)
    if cookie:
        resp.set_cookie("user", cookie)
    return resp

@limiter.limit("5/second")
@app.route('/logout')
def logout_endpoint():
    resp = redirect("/", 302)
    resp.set_cookie('user', '', expires=0)
    return resp

@limiter.limit("5/second")
@app.route('/register', methods=['GET'])
def register_endpoint():
    return render_template("register.html")

@limiter.limit("5/second")
@app.route('/register', methods=['POST'])
def register_endpoint_post():
    user = request.form['user']
    pwd = request.form['pass']
    create_user(user, pwd)
    cookie = login(user, pwd)
    resp = redirect('/me', 302)
    if cookie:
        resp.set_cookie("user", cookie)
    return resp

@limiter.limit("5/second")
@app.route('/user/<userID>')
def user_endpoint(userID):
    user = get_current_user(request)
    conn, cur = get_sql()
    cur.execute("select username from users where user_id = ?", (userID,))
    if row:=cur.fetchone():
        pass
    else:
        cur.close()
        conn.close()
        return "User does not exist!", 404
    cur.close()
    conn.close()
    return f"<h1>{row[0]}</h1>"\
           f"<a href='/'>Home</a><br><a href='/logout'>Logout</a><br><a href='/flag'>Flag</a><br><br>"\
           f"This user has {num_votes(userID)} votes. <a href='/vote/{userID}'>Vote for this user!</a>"

@limiter.limit("5/second")
@app.route('/vote/<userID>')
def vote_endpoint(userID):
    return cast_vote(userID)

@limiter.limit("5/second")
@app.route('/flag')
def flag_endpoint():
    if not voting_ended:
        return "Voting hasn't ended yet!"
    if get_current_id(request) in winners:
        return f"Congrats on being voted most worthy to recieve the flag! {open('flag.txt').read()}"
    return "Doesn't look like you won. Sorry, better luck next time..."

@limiter.limit("5/second")
@app.route('/me')
def me_endpoint():
    user_id = get_current_id(request)
    return redirect(f"/user/{user_id}", 302)


if __name__ == '__main__':
    init()
    conn, cur = get_sql()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            voter_id TEXT UNIQUE ON CONFLICT REPLACE NOT NULL,
            ip_addr TEXT  NOT NULL, 
            vote TEXT NOT NULL
        );'''
    )
    # TODO ip addr needs UNIQUE ON CONFLICT REPLACE
    # removed for testing 
    conn.commit()
    
    app.run('0.0.0.0', 1337)