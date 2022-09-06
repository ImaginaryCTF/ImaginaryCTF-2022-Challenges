import requests
import json

out = []

a = json.loads(requests.get("https://meme-api.herokuapp.com/gimme/wholesomememes/400").text)
for n in a["memes"]:
  print(n["url"])

