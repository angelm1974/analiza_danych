import json
with open('przyklad_a.json', 'r') as plik:
    dane = plik.read()

jsonWartosc = json.loads(dane)
print(jsonWartosc['fruit'])
