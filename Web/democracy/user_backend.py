#!/usr/bin/env python3

from sqlite3 import *
from hashlib import pbkdf2_hmac
from uuid import uuid4

from secret import SECRET

def get_uid():
    u = str(uuid4())
    return u.replace('-', '')

def get_sql():
    conn = connect("users.db")
    cur = conn.cursor()
    return conn, cur

def pass_hash(pwd):
    return pbkdf2_hmac("sha256", pwd.encode(), SECRET, 5000).hex()

def create_user(user, pwd):
    if len(user) <= 0 or len(user) > 512:
        return "Invalid username length!"
    if len(pwd) == 0:
        return "Empty password!"
    hsh = pass_hash(pwd)
    userhsh = pass_hash(user)
    uid = get_uid()
    print(user, pwd, hsh)
    conn, cur = get_sql()
    cur.execute("insert into users values (?, ?, ?, ?)", (user, uid, userhsh, hsh))
    conn.commit()
    cur.close()
    conn.close()
    return "Success!"

def validate_cookie(cookie):
    conn, cur = get_sql()
    cur.execute("select username, user_id from users where cookie = ?", (cookie,))
    if row:=cur.fetchone():
        ret = row[0], row[1]
    else:
        ret = None
    cur.close()
    conn.close()
    return ret

def login(user, pwd):
    hsh = pass_hash(pwd)
    conn, cur = get_sql()
    print(user, hsh)
    cur.execute("select cookie from users where username = ? and password = ?", (user, hsh))
    if row:=cur.fetchone():
        ret = row[0]
    else:
        ret = None
    cur.close()
    conn.close()
    return ret

def get_current_user(request):
    current_hash = request.cookies.get("user")
    ret = validate_cookie(current_hash)
    if ret is None:
        return None
    return ret[0]

def get_current_id(request):
    current_hash = request.cookies.get("user")
    ret = validate_cookie(current_hash)
    if ret is None:
        return None
    return ret[1]

def init():
    conn, cur = get_sql()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE NOT NULL ,
            user_id TEXT UNIQUE NOT NULL ,
            cookie TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        ''')
    conn.commit()
    cur.close()
    conn.close()

def check_id_exists(uid):
    conn, cur = get_sql()
    cur.execute("select username, user_id from users where user_id = ?", (uid,))
    return cur.fetchone()
