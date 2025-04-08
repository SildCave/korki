# requesty
# https to nic innego co http tylko ze z zabezpieczeniami w postaci szyfrowania
# adres ip v4 sklada sie z 4 czesci a mianowicie 4 liczb od 1 do 255 np 242.12.64.198 == bajt.bajt.bajt.bajt
# dns zamienia nam domene w adres ip ktorego moze uzyc nasz komputer

# http to (HyperText Transfer Protocol), HyperText to w zasadzie html
# client i serwer

# żądanie

# GET /index.html HTPP/1.1
# Host: marketplace.visualstudio.com
# User-Agent: Mozilla/5.0
# Accept: text/html

# odpowiedź

# HTTP/1.1 200 OK
# Content-Type: text/html
# Content-Length: 512

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>

# </body>
# </html>

# METODA    | WYKORZYSTANIE

# GET       | bierzemy dane z serwera
# POST      | wysylamy dane do serwera
# PUT       | zaktualizuj cos co juz istnieje
# DELETE    | usuwamy cos

# GET /pogoda?miasto=Warszawa&jednostki=metryczne HTTP/1.1
# Host: api.pogoda.pl

# /pogoda jest naszą scieżką
# miasto=Warszawa&jednostki=metryczne jest naszym query
# w getach dajemy informacje o żądaniu w urla/hiperłącze/linka

# User-Agent informacja o przegladarce ktorej uzywamy
# Accept informacja o tym jakiego formatu oczekujemy np "application/json"
# Authorization "Bearer TOKEN"

# API to (Application Programming Interface)

# STATUS CODE         KATEGORIA        ZNACZENIE
# 200                 KOX              request sie powiodl wszystko kozak
# 201                 KOX              cos zostalo stworzone
# 400                 NIE KOX          zle requesta zrobiliscie
# 401                 NIE KOX          nie zautoryzowany aka nie zalogowany
# 403                 NIE KOX          zabronione kladzie nacisk ze nie macie dostepu
# 404                 NIE KOX          nie znaleziono albo nie istnieje
# 429                 Umiarkowane      spamicie zbyt mocno i serwer tego nie lubi
# 500                 MEGA NIE KOX     serwer sie zesrał

import requests
import json

# pip install requests

print(requests.__version__)

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    print("Wszystko poszlo git")
elif response.status_code == 404:
    print("Nie znaleziono")
else:
    print(f"Error: {response.status_code}")

print("Status Code:", response.status_code)
print("Response Body:", response.json())

response_body = response.json()
print(json.dumps(response_body, indent=4))

print("User ID:", response_body['userId'])

url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId  ^xd": 1
}

response = requests.get(url, params=params)
print("pełen url:", response.url)   # https://jsonplaceholder.typicode.com/posts?userId=1
print(json.dumps(response.json(), indent=4))

headers = {
    "User-Agent": "xdsq browser"
}

response = requests.get("https://httpbin.org/headers", headers=headers)
print(json.dumps(response.json(), indent=4))
