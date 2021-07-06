import datetime

file = open("plik_testowy.txt", "r", encoding="UTF8")
for line in file:
    print(line, end="")
file.close()

with open('plik_testowy.txt', 'r', encoding='UTF8') as plik:
    linie = plik.readlines()
    for linia in linie:
        print(linia.upper(), end="")

dane = ['moje dane 1', 'moje dane 2', 'moje dane 3', 'ąęść', 'lll']


lista3 = []

with open('dane.txt', 'r', encoding='UTF8') as plik:
    linie = plik.readlines()
    for d in linie:
        lista3.append(d.upper().replace('\n', ''))

    print(lista3)

parzyste = list(range(100))[::2]

with open('liczby.txt', 'a',encoding='UTF8')as plik:
    for l in parzyste:
        czas=str(datetime.datetime.now())
        dane=f'{czas} wartość: {l} \n'
        plik.write(dane)
