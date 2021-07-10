import urllib.request as rq
import json
adres = "https://raw.githubusercontent.com/angelm1974/analiza_danych/main/D1/JSON/przyklad_a.json"

dane= rq.urlopen(adres).read().decode('utf-8')

jsonWartosc = json.loads(dane)
print(jsonWartosc['fruit'])
