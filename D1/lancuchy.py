nazwa = "Python"
# nazwa[1]='w'
print(nazwa[1])  # WYCINAMY LITERĘ O INDEXIE 1
print(nazwa[-1])  # WYCINAMY LITERĘ O INDEXIE -1
print(nazwa[1:4])  # WYCINAMY LITERY O INDEXIE 1,2,3
print(nazwa[:])  # WYCINAMY LITERY O INDEXIE od 0 do n - wszystkie
print(nazwa[::2])  # co drugi znak
print(nazwa[1:(len(nazwa)-1)])
nazwa = 5*nazwa
print(nazwa)
print("kot" not in nazwa)
