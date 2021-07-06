from random import randrange, randint, choice, random
miasta = ['Kraków', 'Warszawa', 'Wrocław', 'Poznań', 'Gdańsk', 'Katowice']
print(randrange(0, 100, 2))
print(randint(0, 30))
print(choice(miasta))

with open('dane.csv', 'w', encoding='CP1250')as plik:
    dane = f'"id";"miasto";"temp";"opady"'
    plik.write(dane + '\n')
    for numer in range(1, 101):
        dane = f'{numer};"{choice(miasta)}";{randint(0,30)};{random().__str__().replace(".",",")}'
        plik.write(dane + '\n')
