import requests

url = "https://i.imgur.com/ESyrsPY.png"


resp = requests.get(url)

print(resp.status_code)
