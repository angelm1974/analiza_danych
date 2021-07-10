import urllib.request as rq
import json
from datetime import datetime, timezone, tzinfo

APPID = 'bddff858ac8ab0288ebb62281ed0c169'


def podaj_miasto_kraj(miasto='Rybnik', kraj='pl'):
    dane = miasto.capitalize()
    dane += ',' + kraj.lower()
    return dane


def ui():
    miasto = input("Podaj nazwę miasta: ")
    kraj = input("Podaj dwuliterowy kod kraju: ")
    return(podaj_miasto_kraj(miasto, kraj))


adres_url = f'http://api.openweathermap.org/data/2.5/weather?q={podaj_miasto_kraj()}&units=metric&appid={APPID}'
print(adres_url)

dane = rq.urlopen(adres_url).read()

jsonWartosc = json.loads(dane)

print(jsonWartosc['weather'][0]['description'])
print(datetime.utcfromtimestamp(
    jsonWartosc['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'))
print(jsonWartosc)
# dt = datetime.now
# dt.replace(tzinfo=timezone.utc)
print(datetime.now())
data=datetime(2021,7,8,13,31)
a_delta= data-datetime(1900,1,1)
sek=a_delta.total_seconds()
print(sek)

adres2=f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=60.99&lon=30.9&dt=1625739866&appid={APPID}'
print(adres2)