set1 = set()
set2 = {"Gdańsk", "Warszawa", "Poznań", "Toruń", "Warszawa", "Gdańsk"}
print(set2, type(set2))

nazwa = set("mój Python")
print(nazwa)

a = {1, 2, 3, 4, 5, 6, 7}
b = {5, 6, 7, 8, 9}
print("suma:", a | b)
print("Suma:", a.union(b))

print("Iloczyn: ", a & b)
print('Iloczyn:', a.intersection(b))

print('Różnica a - b:', a-b)
print('Różnica b - a:', b-a)
print('Różnica symetryczna: ', a ^ b)

print('Różnica a - b:', a.difference(b))
print('Różnica b - a:', b.difference(a))
print('Różnica symetryczna: ', a.symmetric_difference(b))

c={0,1,2,3}
d={1,2}
print("Czy zbiór d jest podzbiorem zbioru c:", d.issubset(c))

c.add(4)
c.update(("sadsad"))
c.discard(0)
c.pop()

print(c)

