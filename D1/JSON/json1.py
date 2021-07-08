import json

dane='{"fruit": "Apple","size": "Large","color": "Red"}'

jsonWartosc=json.loads(dane)

print(type(jsonWartosc))