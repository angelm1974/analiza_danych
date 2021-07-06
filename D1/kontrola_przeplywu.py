# x = int(input("Podaj swoją prędkość (km/h): "))

# #SCENARIUSZ 1
# # if x >50:
# #     print("Twoja prędkość jest nieprawidłowa")
# # else:
# #     print("Twoja prędkość jest prawidłowa")

# #SCENARIUSZ 2
# if x >50:
#     print("Twoja prędkość jest nieprawidłowa")
# elif x == 50:
#     print("Twoja prędkość jest aksymalną dozwoloną prędkością")
# elif x < 16:
#     print("TWleczesz się jak żółw")
# else:
#     print("Twoja prędkość jest prawidłowa")

# x = int(input("Podaj pierwszą liczbę: "))
# y = int(input("Podaj drugą liczbę: "))

# if x != y:
#     print('Liczby są różne!!!')
#     if x > y:
#         print(f'liczba {x} jest większa od {y}.')
#     else:
#         print(f'liczba {x} jest mniejsza od {y}.')

# else:
#     print(f'liczba {x} = {y}')

# samogloski=['a','i','o','e','u','y','ó']
# for x in "mój wyraz":
#     if x in samogloski:
#         print(f'{x} - jest samogłoską ')


# liczby=[231,342,645,21,54,2,65,1,996,33]
# for x in liczby:
#     if x %2==0:
#         print(f'{x} - To jest liczba parzysta!')

# a=list(range(1,101))
# print(a)
# for x in a:
#     print(x)

lista = list(range(10))
# # for x in lista:
# #     if x == 7:
# #         break
# #     print(x)

# for x in lista:
#     if x == 5:
#         continue
#     print(x)

# numer = 1
# while numer < 11:
#     if numer % 2 == 0:
#         print(numer)
#     else:
#         print('Liczba nieparzysta')
#     numer += 1

# for x in lista:
#     if x == 0:
#         pass
#     elif x %2 ==0:
#         print(x,'liczba parzysta')
#     else:
#         print(x,'liczba nieparzysta')

kwadraty = []
reszta = []
for a in range(20, 0, -1):
    if a % 3 == 0:
        kwadraty.append(a**2)
    else:
        reszta.append(a)
print(kwadraty)
print(reszta)

l1=list()
l2=list()
for i in range(1,21):
    if i%3==0: l1.insert(0,i*i)
    else: l2.insert(0,i)


lista1=list(range(10,0,-1))
print(lista1)