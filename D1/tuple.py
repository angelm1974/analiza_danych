pusta = tuple()
pusta2 = ()
ola = ("Ola", "z", 23,)
Sara = "Sara", "G", 34,
Olek = 22,
Ola_imie = ola[0]
print(Ola_imie)
print(Olek, type(Olek))

Olek = list(Olek)
Olek.append("U")
Olek.append("33")
Olek = tuple(Olek)
Sara = Sara + Olek
Olek = (22, 'u', 33, True)
Imiona = (Olek, ola, Sara)

print(Imiona, type(Olek))

Romek = ("Romek", "Zakapior", 33, 44, 324, 234)
imie, zawod, *reszta, wiek = Romek
print(imie, zawod, wiek)
members = tuple(list((('Kasia', 23), ('Tomek', 19))).insert(1,('Adam','Henio')))
members = (members[0], ('sadas', "sad"), members[1])
