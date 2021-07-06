def drukuje():
    return 1


a = drukuje()
print(a)


# def imie():
#     return input('Podaj swoje imię')


# b = imie()
# print('Witaj, ', b)


def suma(liczba1, liczba2):
    return liczba1 + liczba2


print(suma(12, 44))


def suma_opcjonalna(liczba1, liczba2=5):
    return liczba1 + liczba2


print(suma_opcjonalna(4))


def suma_wielokrotna(liczba1, *liczba2):
    s2 = sum(liczba2)
    return liczba1 + s2


print(suma_wielokrotna(1, 2))


def funkcja_z_nazwanymi(l1, **kwargs):
    
    return l1 +kwargs.get("pierwszy",10)



print(funkcja_z_nazwanymi(12, pierwszyj=12, drugi=10, trzeci=100))


def make_pizza(rozmiar, *skladniki):
    print(f'wybrales pizze o rozmiarze {rozmiar} z nastepujacymi skaldnikami: ')
    for i in skladniki:
        print(f'- {i}')
    
make_pizza(25,'pomi','szynka')
