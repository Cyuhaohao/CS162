import requests

r=requests.get("https://www.wikipedia.org/")
print(r.html())