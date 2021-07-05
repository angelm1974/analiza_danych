lista = list()
lista1 = []
imiona = ['Ola', 'Ela', 'Jola', 'Kasia']
imiona[1]='Magda'
zmiksowana = ['Python', 12, True, -321.22, "Qwer"]
nested = [[1, 2, 3], ['a', 'b', 'r']]
print(imiona[1])
print(imiona[1:3])

wariacka_lista = [imiona, zmiksowana, nested]
print('wariacka lista', wariacka_lista)
print(wariacka_lista[1])
dodane = imiona+zmiksowana
print(dodane)

lista1.append(33)
print(lista1)
lista1.extend([1, 2,55, 3,2])
print(lista1)
lista1.insert(1,'bubu')
print(lista1)
lista1.remove('bubu')
print(lista1)
print(lista1.pop(3))
#lista1.clear()
print(lista1)
print(lista1.count(2))
lista1.sort()
print(lista1.reverse())
print(lista1)
lista2=lista1.copy()

print('przed cieciem l 1 :',lista1)
print('przed cieciem l 2 :',lista2)
lista2.pop(3)
print('po cieciu l 1: ',lista1)
print('po cieciu l 2: ',lista2)
print(len(lista1))
print(max(lista1))
print(min(lista1))
print(sum(lista1))