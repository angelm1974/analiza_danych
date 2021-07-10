import urllib.request as ur
import json
import csv
import os

adres = 'https://jsonplaceholder.typicode.com/todos/'

with ur.urlopen(adres) as plik:
    dane = plik.read().decode('utf-8')

jsw_w = json.loads(dane)
print(jsw_w)

wyjscie = open("todos.csv", "w", encoding="utf-8", newline="")
o_d_wr = csv.DictWriter(wyjscie, ['userId', 'id', 'title', 'completed'])
o_d_wr.writeheader()

for row in jsw_w:
    o_d_wr.writerow(row)

wyjscie.close()
