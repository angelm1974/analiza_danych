from random import choice

liczby = []
for liczba in range(20):
    if liczba % 2 == 0:
        liczby.append(liczba**2)
print(liczby)

liczby = [x ** 2 for x in range(20) if x % 2 == 0]
print(liczby)


# liczby = [str(x)+'abc' for x in range(20)]
# print(liczby)

# liczby = [(x, 'G'+str(x)) for x in range(20)]
# print(liczby)

# # lista= [wurażenie for zmienna1 in zbior_danych1 for zmienna2 in zbior_danych2]

# litery = "abcdefgh"
# lista = [(x, y) for x in litery for y in range(1, 9)]
# print(lista)

# # rozszerzona lista z 1 warunkiem
# lista = [(x, y, choice(['czarne', 'biale', 'brak']))
#          for x in litery for y in range(1, 9) if y > 5]
# print(lista)

# lista1 = [[j for j in range(10)] for i in range(3)]
# print(lista1)

set1 = {i**2 for i in range(10)}
print(set1)

tekst = '''
Dla obu drużyn będzie to piąty półfinał 
w ich historii startów na mistrzostwach Europy. 
Jak dotychczas Hiszpanie za każdym razem przechodzi
do finału (1964, 1984, 2008 i 2012 r.), natomiast Włosi
trzykrotnie grali później w meczu o złoto (1968, 2000 i 2012 r.),
a raz odpadli. Miało to miejsce w 1988 r., ulegli wówczas ZSRR 0:2.
Od Euro 2008 Squadra Azzurra regularnie, na każdej kolejnej
imprezie mistrzowskiej o puchar Delaunaya, rywalizuje z La Roja.
'''
slowa = tekst.lower().replace('.', '').split()
unikalne = {slowo for slowo in slowa if len(slowo) > 4}
print(unikalne)

imiona = {"Tomek": "Tomasz", "Adam": "Adaś",
          "Zofia": "Zosia", "Katarzyna": "Kasia", "Marek": "Maruś"}

set_imion = {(klucz, wartosc) for (klucz, wartosc) in imiona.items()}
print(set_imion)

odwrocenie = {wartosc: klucz for (klucz, wartosc) in imiona.items()}
print(odwrocenie)


stocks = {'Boombit': 22, 'CD Project': 295,
          'Playway': 350}
stock1 = {klucz: wartosc for(klucz, wartosc) in stocks.items() if wartosc > 100}
print(stock1)