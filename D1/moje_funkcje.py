


def make_pizza(rozmiar, *skladniki):
    print(
        f'wybrales pizze o rozmiarze {rozmiar} z nastepujacymi skaldnikami: ')
    for i in skladniki:
        print(f'- {i}')


def suma_wielokrotna(liczba1, *liczba2):
    s2 = sum(liczba2)
    return liczba1 + s2


def suma_opcjonalna(liczba1, liczba2=5):
    return liczba1 + liczba2


def pobieracz_danych():
    a = input("Podaj imię: ")
    b = input("Podaj Nazwisko: ")
    return {"imie": a, "nazwisko": b}


wynik = pobieracz_danych()
print(wynik)
