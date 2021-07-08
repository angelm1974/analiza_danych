import json

dane = {"fruit": "Apple", "size": "Large", "color": "Red"}

str_dane = json.dumps(dane,separators=('.','-'))
print(str_dane)


str_dane = json.dumps(dane,sort_keys=True, indent=4, separators=(',',':'))
print(str_dane)