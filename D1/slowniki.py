moj_slownik = {"jeden": "abc", "dwa": "cde"}

moj_slownik2 = {0: "abc", 1: "cde"}

osoba = {
    "nazwisko": "Kowalski",
    "imie": "Jan",
    "wiek": 32
}

osoba1 = {
    "nazwisko": "nOWAK",
    "imie": "aDAM",
    "wiek": 22
}
osoba2 = {
    "nazwisko": "Sroka",
    "imie": "Piotr",
    "wiek": 33
}
lista = [osoba, osoba1, osoba2]

for obywatel in lista:
    print(f'dane osoby: {obywatel["nazwisko"]}')
